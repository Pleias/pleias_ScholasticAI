import json
import os
import sys
import shutil
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QListView, QFileDialog, QWidget, QVBoxLayout, QListWidget
from PySide6.QtGui import QStandardItem, QStandardItemModel
from dialog_display import ChatDialog
from ui_forms_v1.ui_chat_window import Ui_MainWindow as ChatWindow
from connect_db import ConnectDB

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIcon

from PyPDF2 import PdfReader
from get_answer_from_api import get_response


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ChatWindow()
        self.ui.setupUi(self)
        self.db = ConnectDB()

        chat_data = [{"title": "Hi, how are you?",
                      "chat_list": [{"input_str": "Hi, how are you?", "out_str": "16 This is model answer"},
                                    {"input_str": "Good and you?", "out_str": "13 This is model answer"}, {
                                        "input_str": "Dark is a dark appearance that doesn\u2019t change. Dark Mode darkens the colour scheme so the content you\u2019re working on stands out, while windows and controls seem to recede into the background. It\u2019s effective for viewing documents, presentations, photos, films, web pages and more.",
                                        "out_str": "278 This is model answer"}]}][0]

        self.scrollArea_2 = self.ui.scrollArea_2
        self.show_chat_window(chat_data)
        self.ui.upload_pdf_btn.clicked.connect(self.upload_files)
        
        # Connect the buttons to functions that change the view
        self.ui.pushButton_3.clicked.connect(self.show_library)  # Library button
        self.ui.pushButton_2.clicked.connect(self.show_conversations)  # Conversations button
        
    def show_library(self):
        """Switch to the Library view and load the list of PDFs."""
        self.ui.stackedWidget.setCurrentWidget(self.ui.library_widget)  # Show the Library view
        self.load_pdf_list()  # Load the list of processed PDFs

    def show_conversations(self):
        """Switch to the Conversations view."""
        self.ui.stackedWidget.setCurrentWidget(self.ui.conversations_widget)  # Show the Conversations view
    
    #### PDF Library Methods ####
    def upload_files(self):
        """Open a file dialog to select one or more PDF files for upload."""
        file_filter = 'Data File (*.pdf);;'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select file(s)',
            dir=os.getcwd(),
            filter=file_filter
        )
        file_paths, _ = response
        for file_path in file_paths:
            self.store_and_save_metadata(file_path)
            print(f"Sucessfully uploaded file at path: {file_path}")
            
    def store_and_save_metadata(self, file_path):
        """Store the PDF file in the local storage directory and save its metadata to the database.
        The metadata is extracted using the extract_metadata method."""
        # Define storage directory
        save_directory = 'app_storage/pdfs'
        os.makedirs(save_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        target_path = os.path.join(save_directory, file_name)

        # Copy the file to the local storage directory
        shutil.copy(file_path, target_path)

        # Extract metadata ====> TO REPLACE WITH CARLOS FUNCTION
        metadata = self.extract_metadata(file_path) 

        # Save metadata to database
        self.db.insert_pdf_metadata(file_name, target_path, metadata)
        
        
    def extract_metadata(self, file_path):
        """Extract metadata from a PDF file using the PyPDF2 library.
        TO REPLACE WITH CARLOS FUNCTION"""
        with open(file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            info = pdf_reader.metadata
            metadata = {
                'title': info.title if info.title else "Untitled",
                'author': info.author if info.author else "Unknown",
                'creation_date': info['/CreationDate'] if '/CreationDate' in info else "N/A",
                'subject': info.subject if info.subject else "N/A"
            }
        return metadata
        
    def closeEvent(self, event):
        """Close the database connection when the main window is closed"""
        self.db.close()
        event.accept()
        

    def load_pdf_list(self):
        """Load the list of processed PDFs into the Library view."""
        self.ui.pdf_list_widget.clear()  # Clear the current list

        # Retrieve PDF metadata from the database
        pdf_metadata_list = self.db.get_all_pdf_metadata()  # Assuming this method returns a list of PDFs
        
        # Add each PDF to the QListWidget
        for pdf_metadata in pdf_metadata_list:
            file_name = pdf_metadata[1]  # Assuming index 1 is the file name
            file_path = pdf_metadata[2]  # Assuming index 2 is the file path
            self.ui.pdf_list_widget.addItem(f"{file_name} - {file_path}")

    #### Chat Window Methods ####
    def show_chat_window(self, chat_data):
        grid_layout = self.scrollArea_2
        dialog = ChatDialog(chat_data)
        grid_layout.setWidget(dialog)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and show the main window
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
