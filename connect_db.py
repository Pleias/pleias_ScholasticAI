import sqlite3
import json
import os


class ConnectDB:
    def __init__(self):
        self.chat_db_path = "app_storage/chat_data/data.json"

        # New database for PDF metadata storage
        self.pdf_db_path = "app_storage/metadata/pdf_documents.db"
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

    def init_pdf_database(self):
        """Creates the SQLite database for PDF metadata if it doesn’t already exist."""
        if not os.path.exists(self.pdf_db_path):
            connection = sqlite3.connect(self.pdf_db_path)
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pdf_metadata (
                    id INTEGER PRIMARY KEY,
                    file_name TEXT,
                    file_path TEXT,
                    title TEXT,
                    author TEXT,
                    creation_date TEXT,
                    subject TEXT
                )
            ''')
            connection.commit()
            connection.close()

    def insert_pdf_metadata(self, file_name, file_path, metadata):
        """Inserts metadata for a PDF into the database.
        Accepts file_name, file_path, and a dictionary of metadata fields."""
        connection = sqlite3.connect(self.pdf_db_path)
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO pdf_metadata (file_name, file_path, title, author, creation_date, subject)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (file_name, file_path, metadata.get('title'), metadata.get('author'),
              metadata.get('creation_date'), metadata.get('subject')))
        connection.commit()
        connection.close()

    def get_all_pdf_metadata(self):
        """Retrieves all entries in the pdf_metadata table, 
        useful for loading and displaying metadata if needed in the app."""
        connection = sqlite3.connect(self.pdf_db_path)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pdf_metadata')
        pdf_metadata = cursor.fetchall()
        connection.close()
        return pdf_metadata

    def delete_pdf_metadata(self, pdf_id):
        """Deletes a specific entry in the pdf_metadata table based on the id (primary key), 
        allowing you remove a record if necessary."""
        connection = sqlite3.connect(self.pdf_db_path)
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pdf_metadata WHERE id = ?', (pdf_id,))
        connection.commit()
        connection.close()

    def close(self):
        # Placeholder close method to prevent errors; add actual cleanup if needed
        pass
