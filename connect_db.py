import shutil
import sqlite3
import sqlite_vec
import json
import os

from PyPDF2 import PdfReader


class ConnectDB:
    def __init__(self):
        self.chat_db_path = "app_storage/chat_data/data.json"

        # Database to database
        self.db_path = "app_storage/metadata/sqlite-poc.db"
        self.init_pdf_database()

    def get_chat_data(self):
        with open(self.chat_db_path, "r") as f:
            chat_db = json.load(f)

        return chat_db

    def get_chat_title_list(self):
        chat_list = []
        chat_db = self.get_chat_data()
        for chat in chat_db:
            title = chat.get("title")
            chat_list.append(title)
        return chat_list

    def save_chat_data(self, new_chat_data):
        with open(self.chat_db_path, "w") as f:
            f.write(json.dumps(new_chat_data))

    def delete_all_data(self):
        chat_db = self.get_chat_data()
        chat_db.clear()
        self.save_chat_data(chat_db)

    def delete_chat_data(self, index):
        with open(self.chat_db_path, "r") as f:
            chat_db = json.load(f)
        chat_db.pop(index)

        self.save_chat_data(chat_db)

    ### PDF Metadata Storage Methods ###

    def init_database(self):
        """Creates the SQLite database if it doesn’t already exist.
        Creates the 3 tables: pdf_metadata, chunks, and chunk_embeddings.""" 

        if not os.path.exists(self.db_path):
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            # Metadata table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pdf_metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_name TEXT,
                    file_path TEXT,
                    title TEXT,
                    author TEXT,
                    creation_date TEXT,
                    subject TEXT
                )
            """)
            # Chunks table: we can add fields
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS chunks (
                    chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    section TEXT,
                    sentence TEXT,
                    pages TEXT,
                    word_count INTEGER,
                    document_id INTEGER
                    )
                """
            )
            # Embeddings table
            cursor.enable_load_extension(True)
            sqlite_vec.load(cursor)
            cursor.enable_load_extension(False)
            cursor.execute("""
                    CREATE VIRTUAL TABLE IF NOT EXISTS chunk_embeddings USING vec0(
                    chunk_id INTEGER PRIMARY KEY,
                    embedding float[4],
                """
            ) # replace 4 with the actual size of the embedding

            connection.commit()
            connection.close()
            
    def insert_pdf_metadata(self, file_name, file_path, metadata, verbose=True):
        """Inserts metadata for a PDF into the database.
        Accepts file_name, file_path, and a dictionary of metadata fields."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO pdf_metadata (file_name, file_path, title, author, creation_date, subject)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (file_name, file_path, metadata.get('title'), metadata.get('author'),
              metadata.get('creation_date'), metadata.get('subject')))
        if verbose:
            print(f"Inserted metadata for {file_name}")
        connection.commit()
        connection.close()
        
    def insert_chunks(self, chunks, document_id, verbose=True):
        """"Accepts a list of chunks. The document_id is the id of the document in the metadata table.
        Returns a list of the new chunk ids, which is useful to embed these new chunks afterwards."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        new_ids = []
        for chunk in chunks:
            cursor.execute("""
                INSERT INTO chunks (section, text, pages, word_count, document_id)
                VALUES (?, ?)
            """, (chunk["section"], chunk["text"], chunk["pages"], chunk["word_count"], document_id))
            new_ids.append(cursor.lastrowid)
        if verbose:
            print(f"Inserted {len(chunks)} chunks for document {document_id}")
        connection.commit()
        connection.close()
        return new_ids
    
    def insert_embeddings(self, chunk_ids, verbose=True):
        """Accepts a list of chunk ids and a list of embeddings. Inserts the embeddings into the database."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        for chunk_id in chunk_ids:
            cursor.execute("""
                SELECT sentence FROM pdf_metadata WHERE chunk_id = ?
            """, (id))
            sentence = cursor.fetchone()[0]
            embedding = embed(sentence) #### NOTE: we have to create an embedding function
            cursor.execute("""
                INSERT INTO chunk_embeddings (chunk_id, embedding)
                VALUES (?, ?)
            """, (chunk_id, embedding))
            if verbose:
                print(f"Inserted embedding for chunk {chunk_id}")
        connection.commit()
        connection.close()
        

    def get_all_pdf_metadata(self):
        """Retrieves all entries in the pdf_metadata table, 
        useful for loading and displaying metadata if needed in the app."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pdf_metadata')
        pdf_metadata = cursor.fetchall()
        connection.close()
        return pdf_metadata

    def delete_pdf_metadata(self, pdf_id):
        """Deletes a specific entry in the pdf_metadata table based on the id (primary key), 
        allowing you remove a record if necessary."""
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pdf_metadata WHERE id = ?', (pdf_id,))
        connection.commit()
        connection.close()

    def store_pdf(self, file_path):
        """Store the PDF file in the local storage directory."""
        # Define storage directory
        save_directory = 'app_storage/pdfs'
        os.makedirs(save_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        target_path = os.path.join(save_directory, file_name)
        # Copy the file to the local storage directory
        if not os.path.exists(target_path):
            shutil.copy(file_path, target_path)

    def close(self):
        # Placeholder close method to prevent errors; add actual cleanup if needed
        pass
