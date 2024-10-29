import json
import os
import sys
import shutil
from typing import List, Optional

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QListView, QFileDialog, QWidget, \
    QVBoxLayout, QListWidget
from PySide6.QtGui import QStandardItem, QStandardItemModel
from dialog_display import ChatDialog
from ui_forms_v1.ui_chat_window2 import Ui_MainWindow as ChatWindow
from ui_forms_v1.uploaded_docs_widget import Ui_Frame as DocsWidget
from ui_forms_v1.reference_ui import Ui_Form as ReferenceForm
from connect_db import ConnectDB

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIcon

from PyPDF2 import PdfReader
from get_answer_from_api import get_response

chat_data = [{"title": "Hi, how are you?",
              "chat_list": [{"input_str": "Hi, how are you?", "out_str": "16 This is model answer"},
                            {"input_str": "Good and you?", "out_str": "13 This is model answer"}, {
                                "input_str": "Dark is a dark appearance that doesn\u2019t change. Dark Mode darkens the colour scheme so the content you\u2019re working on stands out, while windows and controls seem to recede into the background. It\u2019s effective for viewing documents, presentations, photos, films, web pages and more.",
                                "out_str": "278 This is model answer"}]}][0]


class ReferenceWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        # Initialize of the main window
        self.ui = ReferenceForm()
        self.ui.setupUi(self)
        self.ui.label_2.setText(text)


class UploadedDocs(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = DocsWidget()
        self.ui.setupUi(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ChatWindow()
        self.ui.setupUi(self)
        self.db = ConnectDB()
        self.dialog_is_empty = True
        self.sources_is_empty = True

        # self.conversation_frame = self.ui.conversation_frame
        # self.ui.conversation_btn.clicked.connect(self.show_lower_frame)
        # self.show_conversation_frame()

        # Upload button clicked
        self.ui.upload_pdf_btn.clicked.connect(self.upload_files)
        # Send msg clicked
        self.ui.msg_send_btn.clicked.connect(self.get_response)

        # Hide scrollbar of scroll area
        self.ui.main_sroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.show_conversation_frame()

    def get_response(self):
        message_input = self.ui.msg_input_text_edit.toPlainText().strip()
        chat_db = self.db.get_chat_data()
        if message_input:
            source_documents, response_str = get_response(message_input, debug=True)
            if not self.dialog_is_empty:
                # Get current selected chat index
                select_row = 0  # In the future it must be project id

                chat_db[select_row]["chat_list"] += [{"input_str": message_input, "out_str": response_str}]
                chat_data = chat_db[select_row]

                self.db.save_chat_data(chat_db)
                self.show_conversation_frame(chat_data)
                # self.show_reference_list(source_documents)

            else:
                # Create new chat and save it into database
                self.dialog_is_empty = False
                chat_data = {
                    "title": message_input,
                    "chat_list": [
                        {
                            "input_str": message_input,
                            "out_str": response_str
                        }
                    ]
                }
                chat_db.insert(0, chat_data)
                self.db.save_chat_data(chat_db)

                # Reload window
                self.show_conversation_frame(chat_data)
                # self.show_reference_list(source_documents)

            ## Clear input after get response
            self.ui.msg_input_text_edit.clear()
            return

    def show_lower_frame(self):
        """
        In the upper frame we have several buttons, such as Library, Projects, About, Login IN
        This function is used to display the lower frame corresponding to one of the buttons
        For example display conversation_frame if conversation_btn is clicked etc
        """
        pass

    def show_conversation_frame(self, chat_data=None) -> None:
        """
        We have 3 different states for conversation frame. First case is showed by default
            1. User didn't upload any documents yet and haven't started the conversation
            2. User have uploaded a document and haven't started the conversation
            3. User have started the conversation

        """
        if self.dialog_is_empty and not self.sources_is_empty:
            state_widget = UploadedDocs()
            grid_layout = self.ui.main_sroll_area
            grid_layout.setWidget(state_widget)

        if not self.dialog_is_empty and not self.sources_is_empty:
            grid_layout = self.ui.main_sroll_area
            dialog = ChatDialog(chat_data)
            grid_layout.setWidget(dialog)

    def upload_files(self):
        """Open a file dialog to select one or more PDF files for upload."""
        self.sources_is_empty = False
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

        self.show_reference_list(file_paths)
        self.show_conversation_frame()

    def store_and_save_metadata(self, file_path):
        """Store the PDF file in the local storage directory and save its metadata to the database.
        The metadata is extracted using the extract_metadata method."""
        # Define storage directory
        save_directory = 'app_storage/pdfs'
        os.makedirs(save_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        target_path = os.path.join(save_directory, file_name)

        # Copy the file to the local storage directory
        if not os.path.exists(target_path):
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

    def show_reference_list(self, document_list: List[str]):
        # Create QStandardItemModel for show chat title list
        model = QStandardItemModel()
        self.ui.uploaded_docs_list.setModel(model)
        # Get chat title list from database
        for document in document_list:
            item = QStandardItem()
            model.appendRow(item)

            index = item.index()

            widget = ReferenceWidget(document)
            self.ui.uploaded_docs_list.setIndexWidget(index, widget)

        # Set spacing and margins
        self.ui.uploaded_docs_list.setSpacing(10)
        self.ui.uploaded_docs_list.setContentsMargins(5, 0, 5, 5)
        # self.ui.uploaded_docs_list.setViewMode(QListView.IconMode)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
