import shutil
import sqlite3
import sqlite_vec
import json
import os
from typing import List, Dict, Sequence, Any

from src.core.pdf_processing_pipeline import process_pdfs_in_folder
from src.core.embedding import embed_query, format_for_vec_db


class ConnectDB:
    def __init__(
        self,
        chat_db_path: str = "app_storage/chat_data/data.json",
        db_path: str = "app_storage/metadata/chunks_and_pdfs.db",
    ):
        # Init folders and database
        self.chat_db_path = chat_db_path
        self.db_path = db_path
        self.ensure_files_exist()
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

    def save_chat_data(self, new_chat_data: Dict[str, str]):
        with open(self.chat_db_path, "w") as f:
            f.write(json.dumps(new_chat_data))

    def delete_all_data(self):
        chat_db = self.get_chat_data()
        chat_db.clear()
        self.save_chat_data(chat_db)

    def delete_chat_data(self, index: int):
        with open(self.chat_db_path, "r") as f:
            chat_db = json.load(f)
        chat_db.pop(index)

        self.save_chat_data(chat_db)

    def ensure_files_exist(self):
        """Ensure all required directories exist."""
    
        required_folders = [
            "app_storage/pdfs/processed",
            "app_storage/pdfs/to_process",
            "app_storage/chat_data",
            "app_storage/metadata",
        ]
        for folder in required_folders:
            os.makedirs(folder, exist_ok=True)
            
        if not os.path.exists(self.chat_db_path):
            with open(self.chat_db_path, "w") as f:
                json.dump([], f) 

        
    def init_database(self):
        """Creates the SQLite database if it does not already exist.
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
                    document_id INTEGER,
                    hash TEXT
                    )
                """
            )
            # Chunks table for FTS
            cursor.execute("""
            CREATE VIRTUAL TABLE chunks_fts USING fts5(
                text,
                content='chunks', content_rowid='chunk_id'
                )
            """)

            # Embeddings table
            cursor.execute("""
                    CREATE VIRTUAL TABLE IF NOT EXISTS chunk_embeddings USING vec0(
                    chunk_id INTEGER PRIMARY KEY,
                    embedding float[384] distance_metric=cosine)
                """)  # cosine similarity

            self.connection.commit()

    def insert_pdf_metadata(
        self, file_name: str, metadata: Dict[str, Any], verbose: bool = True
    ):
        """Inserts metadata for a PDF into the database.
        Accepts file_name, and a dictionary of metadata fields."""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT INTO pdf_metadata (
                file_name, title, author, subject, keywords, creation_date
                )
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                file_name,
                metadata.get("title"),
                metadata.get("author"),
                metadata.get("subject"),
                metadata.get("keywords"),
                metadata.get("creation_date"),
            ),
        )
        if verbose:
            print(f"Inserted metadata for {file_name}")
        ids = cursor.lastrowid
        self.connection.commit()
        return ids

    def insert_chunks(
        self, chunks: Sequence[str], document_id: int, verbose: bool = True
    ):
        """Accepts a list of chunks. The document_id is the id of the document in the metadata table.
        Returns a list of the new chunk ids, which is useful to embed these new chunks afterward."""
        cursor = self.connection.cursor()
        new_ids = []
        for chunk in chunks:
            cursor.execute(
                """
                INSERT INTO chunks (section, text, pages, word_count, document_id, hash)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    chunk["section"],
                    chunk["text"],
                    str(chunk["pages"]),
                    chunk["word_count"],
                    document_id,
                    chunk["hash"],
                ),
            )
            last_id = cursor.lastrowid
            cursor.execute(
                """
                INSERT INTO chunks_fts(rowid, text)
                VALUES (?, ?)
            """,
                (last_id, chunk["text"]),
            )
            new_ids.append(last_id)
        if verbose:
            print(f"Inserted {len(chunks)} chunks for document n°{document_id}")
        self.connection.commit()
        return new_ids

    def insert_embeddings(self, new_chunk_ids: Sequence[int], verbose: bool = True):
        """Accepts a list of chunk ids. Inserts the embeddings into the database."""

        cursor = self.connection.cursor()
        placeholders = ", ".join("?" for _ in new_chunk_ids)
        cursor.execute(
            f"""
            SELECT text FROM chunks WHERE chunk_id IN ({placeholders})
        """,
            new_chunk_ids,
        )
        chunks = cursor.fetchall()
        chunks = [chunk[0] for chunk in chunks]

        if verbose:
            print("Embedding chunks")
        embeddings = embed_query(chunks)

        if verbose:
            print("Inserting embeddings")
        for chunk_id, embedding in zip(new_chunk_ids, embeddings):
            # Embed text and store it
            cursor.execute(
                """
                INSERT INTO chunk_embeddings (chunk_id, embedding)
                VALUES (?, ?)
            """,
                (chunk_id, format_for_vec_db(embedding)),
            )

        if verbose:
            print("Inserted embeddings")

        self.connection.commit()

    def parse_pdf_to_db(
        self,
        parsed_pdf_list: List[dict] = None,
        verbose: bool = True,
        pdf_folder: str = "app_storage/pdfs/to_process",
        yolo_model_path: str = "models/yolo.pt",
        intermediate_store_folder: str = None,
        pdf_chunk_size: int = 25,
        batch_size: int = 10,
    ):
        # to combine the functions earlier in a single function
        # combine with pdf parsing function
        if parsed_pdf_list is None:
            parsed_pdf_list = process_pdfs_in_folder(
                pdf_folder=pdf_folder,
                yolo_model_path=yolo_model_path,
                output_folder=intermediate_store_folder,
                pdf_chunk_size=pdf_chunk_size,
                batch_size=batch_size,
            )

        for parsed_pdf in parsed_pdf_list:
            file_name = parsed_pdf.get("document_name")
            metadata = parsed_pdf.get("metadata")

            # Insert metadata
            document_id = self.insert_pdf_metadata(
                file_name=file_name, metadata=metadata, verbose=verbose
            )

            # Insert chunks
            chunks = parsed_pdf.get("sections")
            new_chunk_ids = self.insert_chunks(
                chunks=chunks, document_id=document_id, verbose=verbose
            )

            # Insert embeddings
            self.insert_embeddings(new_chunk_ids=new_chunk_ids, verbose=verbose)

            if verbose:
                print(f"Stored metadata, chunks, and embeddings for {file_name}")
                print("-------------------")

        if verbose:
            print("All PDFs parsed successfully.")

    def get_all_pdf_metadata(self):
        """Retrieves all entries in the pdf_metadata table,
        useful for loading and displaying metadata if needed in the app."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM pdf_metadata")
        pdf_metadata = cursor.fetchall()
        return pdf_metadata

    def delete_pdf_metadata(self, pdf_id: int):
        """Deletes a specific entry in the pdf_metadata table based on the id (primary key),
        allowing you remove a record if necessary."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM pdf_metadata WHERE id = ?", (pdf_id,))
        self.connection.commit()

    @staticmethod
    def store_pdf(file_path: str):
        """Store the PDF file in the local storage directory."""
        # Define storage directory
        save_directory = "app_storage/pdfs/to_process"
        os.makedirs(save_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        target_path = os.path.join(save_directory, file_name)
        # Copy the file to the local storage directory
        if not os.path.exists(target_path):
            shutil.copy(file_path, target_path)

    @staticmethod
    def move_pdf(old_path: str, new_path: str):
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

if __name__ == "__main__":
    db = ConnectDB()
    db.parse_pdf_to_db()
    db.close()