import shutil
import sqlite3
import sqlite_vec
import json
import os
import struct
from typing import List
import numpy as np

from PyPDF2 import PdfReader

from pdf_processing_pipeline import process_pdfs_in_folder

class ConnectDB:
    def __init__(self, 
                 chat_db_path="app_storage/chat_data/data.json", 
                 db_path="app_storage/metadata/sqlite-poc.db"):
        self.chat_db_path = chat_db_path

        # Database to database
        self.db_path = db_path
        
        self.init_database()
        
        # Persistent connection
        self.connection = sqlite3.connect(self.db_path)  
        self.connection.enable_load_extension(True)
        sqlite_vec.load(self.connection)
        self.connection.enable_load_extension(False)
        

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
        Creates the 4 tables: pdf_metadata, chunks, chunks for FTS, and chunk_embeddings.""" 

        if not os.path.exists(self.db_path):
            
            self.connection = sqlite3.connect(self.db_path)  
            self.connection.enable_load_extension(True)
            sqlite_vec.load(self.connection)
            self.connection.enable_load_extension(False)
            cursor = self.connection.cursor()
            
            print("Creating database and tables...")

            # Metadata table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pdf_metadata (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_name TEXT,
                    title TEXT,
                    author TEXT,
                    subject TEXT,
                    keywords TEXT,
                    creation_date TEXT
                )
            """)
            # Chunks table
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS chunks (
                    chunk_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    section TEXT,
                    text TEXT,
                    pages TEXT,
                    word_count INTEGER,
                    document_id INTEGER
                    )
                """
            )
            # Chunks table for FTS
            cursor.execute("""
            CREATE VIRTUAL TABLE fts_chunks USING fts5(
                text,
                content='chunks', content_rowid='chunk_id'
                )
            """
            )
            
            # Embeddings table
            cursor.execute("""
                    CREATE VIRTUAL TABLE IF NOT EXISTS chunk_embeddings USING vec0(
                    chunk_id INTEGER PRIMARY KEY,
                    embedding float[4])
                """
            ) # replace 4 with the actual size of the embedding

            self.connection.commit()
            
    def insert_pdf_metadata(self, file_name, metadata, verbose=True):
        """Inserts metadata for a PDF into the database.
        Accepts file_name, and a dictionary of metadata fields."""
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO pdf_metadata (
                file_name, title, author, subject, keywords, creation_date
                )
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (file_name, 
              metadata.get('title'), 
              metadata.get('author'),
              metadata.get('subject'),
              metadata.get('keywords'),
              metadata.get('creation_date')))
        if verbose:
            print(f"Inserted metadata for {file_name}")
        id = cursor.lastrowid
        self.connection.commit()
        return id
        
    def insert_chunks(self, chunks, document_id, verbose=True):
        """"Accepts a list of chunks. The document_id is the id of the document in the metadata table.
        Returns a list of the new chunk ids, which is useful to embed these new chunks afterwards."""
        cursor = self.connection.cursor()
        new_ids = []
        for chunk in chunks:
            cursor.execute("""
                INSERT INTO chunks (section, text, pages, word_count, document_id)
                VALUES (?, ?, ?, ?, ?)
            """, (chunk["section"], chunk["text"], str(chunk["pages"]), chunk["word_count"], document_id))
            last_id = cursor.lastrowid
            cursor.execute("""
                INSERT INTO fts_chunks(rowid, text)
                VALUES (?, ?)
            """, (last_id, chunk["text"]))
            new_ids.append(last_id)
        if verbose:
            print(f"Inserted {len(chunks)} chunks for document {document_id}")
        self.connection.commit()
        return new_ids
    
    def embed(self, text):
        # Placeholder function to generate embeddings
        return [np.random.rand() for i in range(4)] # Placeholder embedding
    
    def serialize_f32(self, vector: List[float]) -> bytes:
        """serializes a list of floats into a compact "raw bytes" format"""
        return struct.pack("%sf" % len(vector), *vector)
    
    def insert_embeddings(self, new_chunk_ids, verbose=True):
        """Accepts a list of chunk ids. Inserts the embeddings into the database."""

        cursor = self.connection.cursor()
        for chunk_id in new_chunk_ids:
            # Extract text from the chunk
            cursor.execute("""
                SELECT text FROM chunks WHERE chunk_id = ?
            """, (chunk_id,))
            text = cursor.fetchone()[0]
            
            # Embed text and store it
            embedding = self.serialize_f32(self.embed(text)) #### NOTE: we have to create an embedding function
            cursor.execute("""
                INSERT INTO chunk_embeddings (chunk_id, embedding)
                VALUES (?, ?)
            """, (chunk_id, embedding))
        cursor.execute("INSERT INTO fts_chunks(fts_chunks) VALUES('optimize')")
        
        if verbose:
            print(f"Inserted embeddings")
            
        self.connection.commit()
        
        
    def parse_pdf_to_db(self, 
                         parsed_pdf_list=None,
                         verbose=True,
                         pdf_folder="app_storage/pdfs/to_process", 
                         yolo_model_path="models/yolo.pt", 
                         intermediate_store_folder=None, 
                         pdf_chunk_size=25, 
                         batch_size=10):
        # to combine the functions earlier in a single function
        # combine with pdf parsing function
        if parsed_pdf_list is None:
            parsed_pdf_list = process_pdfs_in_folder(pdf_folder=pdf_folder, 
                            yolo_model_path=yolo_model_path, 
                            output_folder=intermediate_store_folder, 
                            pdf_chunk_size=pdf_chunk_size, 
                            batch_size=batch_size)
        
        for parsed_pdf in parsed_pdf_list:
            file_name = parsed_pdf.get("document_name")
            metadata = parsed_pdf.get("metadata")
            
            # Insert metadata
            document_id = self.insert_pdf_metadata(file_name=file_name, 
                                                   metadata=metadata, 
                                                   verbose=verbose)
            
            # Insert chunks
            chunks = parsed_pdf.get("sections")
            new_chunk_ids = self.insert_chunks(chunks=chunks, 
                                               document_id=document_id, 
                                               verbose=verbose)
            
            # Insert embeddings
            self.insert_embeddings(new_chunk_ids=new_chunk_ids, 
                                   verbose=verbose)
            
            if verbose:
                print(f"Stored metadata, chunks, and embeddings for {file_name}")
            
        if verbose:
            print("All PDFs parsed successfully.")
            
        

    def get_all_pdf_metadata(self):
        """Retrieves all entries in the pdf_metadata table, 
        useful for loading and displaying metadata if needed in the app."""
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM pdf_metadata')
        pdf_metadata = cursor.fetchall()
        return pdf_metadata

    def delete_pdf_metadata(self, pdf_id):
        """Deletes a specific entry in the pdf_metadata table based on the id (primary key), 
        allowing you remove a record if necessary."""
        cursor = self.connection.cursor()
        cursor.execute('DELETE FROM pdf_metadata WHERE id = ?', (pdf_id,))
        self.connection.commit()

    def store_pdf(self, file_path):
        """Store the PDF file in the local storage directory."""
        # Define storage directory
        save_directory = 'app_storage/pdfs/to_process'
        os.makedirs(save_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        target_path = os.path.join(save_directory, file_name)
        # Copy the file to the local storage directory
        if not os.path.exists(target_path):
            shutil.copy(file_path, target_path)

    def move_pdf(self, old_path, new_path):
        """Move a PDF file from one location to another."""
        for item in os.listdir(old_path):
            item_old_path = os.path.join(old_path, item)
            item_new_path = os.path.join(new_path, item)
            
            # # Remove it already exists
            if os.path.exists(item_new_path):
                os.remove(item_new_path)
                
            shutil.move(item_old_path, new_path)

    def close(self):
        """Close the persistent database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")