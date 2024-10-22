import json
import os
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QListView, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
from dialog_display import ChatDialog
from ui_forms_v1.ui_chat_window import Ui_MainWindow as ChatWindow
from connect_db import ConnectDB

from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit
from PySide6.QtGui import QIcon

from get_answer_from_api import get_response


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ChatWindow()
        self.ui.setupUi(self)

        chat_data = [{"title": "Hi, how are you?",
                      "chat_list": [{"input_str": "Hi, how are you?", "out_str": "16 This is model answer"},
                                    {"input_str": "Good and you?", "out_str": "13 This is model answer"}, {
                                        "input_str": "Dark is a dark appearance that doesn\u2019t change. Dark Mode darkens the colour scheme so the content you\u2019re working on stands out, while windows and controls seem to recede into the background. It\u2019s effective for viewing documents, presentations, photos, films, web pages and more.",
                                        "out_str": "278 This is model answer"}]}][0]

        self.scrollArea_2 = self.ui.scrollArea_2
        self.show_chat_window(chat_data)
        self.ui.upload_pdf_btn.clicked.connect(self.upload_files)

    def upload_files(self):
        file_filter = 'Data File (*.pdf);;'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select file(s)',
            dir=os.getcwd(),
            filter=file_filter
        )
        file_names, _ = response
        return None

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
