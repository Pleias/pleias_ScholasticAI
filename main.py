import os
import sys
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PySide6.QtWidgets import QWidget
from connect_db import ConnectDB
from dialog_display import ChatDialog
from get_answer_from_api import get_response_and_metadata
from ui_forms_v1.reference_ui import Ui_Form as ReferenceForm
from ui_forms_v1.ui_chat_window import Ui_MainWindow as ChatWindow
from ui_forms_v1.ui_uploaded_docs_widget import Ui_user_prompts as DocsWidget

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ReferenceWidget(QWidget):
    def __init__(self, text):
        super().__init__()

        # Initialize of the main window
        self.ui = ReferenceForm()
        self.ui.setupUi(self)
        self.ui.label_2.setText(text)

class UploadedDocs(QWidget):
    """
    This is a screen which user see after uploading documents.
    """

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

        # Resize input frame and textEdit
        self.ui.msg_input_frame.setFixedHeight(45)
        self.ui.msg_input_text_edit.setFixedHeight(45)

        # Adjust input height by text height
        # Upload button clicked
        self.ui.upload_pdf_btn.clicked.connect(self.upload_files)
        # Process button clicked
        # self.ui.process_btn.clicked.connect(self.process_files)
        # Send msg clicked
        self.ui.msg_send_btn.clicked.connect(self.get_response)

        # Hide scrollbar of scroll area
        self.ui.main_sroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.show_conversation_frame()

        # OPEN ALEX BTN
        self.ui.open_alex_btn.setCheckable(True)
        self.ui.open_alex_btn.setStyleSheet("""
            QPushButton {
                background-color: none;
            }
            QPushButton:checked {
                background-color: grey;
            }
        """)

        # ARCHIVE BTN
        self.ui.archive_btn.setCheckable(True)
        self.ui.archive_btn.setStyleSheet("""
            QPushButton {
                background-color: none;
            }
            QPushButton:checked {
                background-color: grey;
            }
        """)

    def closeEvent(self, event):
        """Overide closing method to make sure the database connection is closed"""
        self.db.close()  # Close the database connection
        event.accept()  # Accept the close event

    def archive_btn_clicked(self):
        pass

    def open_alex_btn(self):
        if self.ui.open_alex_btn.isChecked():
            print(
                "if this btn is clicked we have to find 3 the most similar text chunks??"
                "add them to our prompt"
            )
        else:
            print("Button is not pressed.")

    def on_msg_input_text_edit(self):
        document = self.ui.msg_input_text_edit.document()
        self.ui.msg_input_text_edit.setFixedHeight(int(document.size().height()))
        self.ui.msg_input_frame.setFixedHeight(int(document.size().height()))

    def get_response(self):
        message_input = self.ui.msg_input_text_edit.toPlainText().strip()
        chat_db = self.db.get_chat_data()
        if message_input:
            open_alex = self.ui.open_alex_btn.isChecked()
            #print("IN MAIN, CALLING GET_RESPONSE_AND_METADATA")
            references_info, html_output = get_response_and_metadata(message_input, open_alex)
            if not self.dialog_is_empty:
                #print("IN MAIN, DIALOG IS NOT EMPTY")
                # Get current selected chat index
                select_row = 0  # In the future it must be project id

                chat_db[select_row]["chat_list"] += [
                    {
                        "input_str": message_input,
                        "out_str": html_output,
                        "references_info": references_info,
                    }
                ]
                chat_data = chat_db[select_row]
                #print("chat_db : ",chat_db)
                #print("chat_data : ",chat_data)
                self.db.save_chat_data(chat_db)
                #print("calling show_conversation_frame")
                self.show_conversation_frame(chat_data)
                # self.show_reference_list(source_documents)

            else:
                #print("IN MAIN, DIALOG IS EMPTY")
                # Create new chat and save it into database
                self.dialog_is_empty = False
                chat_data = {
                    "title": message_input,
                    "chat_list": [
                        {
                            "input_str": message_input,
                            "out_str": html_output,
                            "references_info": references_info,
                        }
                    ],
                }
                chat_db.insert(0, chat_data)
                #print("chat_db : ",chat_db)
                #print("chat_data : ",chat_data)
                self.db.save_chat_data(chat_db)

                #print("calling show_conversation_frame")
                # Reload window
                self.show_conversation_frame(chat_data)

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
        ###DEBUG
        print("#####################DEBUG MODE###########################")
        print(f"dialog_is_empty: {self.dialog_is_empty}")
        print(f"sources_is_empty: {self.sources_is_empty}")
        print(f"chat_data: {chat_data}")
        
        self.sources_is_empty = False

        if self.dialog_is_empty and not self.sources_is_empty:
            print("State 2: Documents uploaded but no conversation yet")
            state_widget = UploadedDocs()
            grid_layout = self.ui.main_sroll_area
            grid_layout.setWidget(state_widget)
        elif not self.dialog_is_empty and not self.sources_is_empty:
            print("State 3: Active conversation")
            grid_layout = self.ui.main_sroll_area
            # If no chat_data is provided, preserve the existing widget
            if chat_data is None:
                print("Maintaining current conversation view")
                return
                
            dialog = ChatDialog(chat_data)
            grid_layout.setWidget(dialog)
            scroll_bar = self.ui.main_sroll_area.verticalScrollBar()
            scroll_bar.setValue(scroll_bar.maximum())

    def upload_files(self):
        """Open a file dialog to select one or more PDF files for upload."""
        self.sources_is_empty = False
        file_filter = "Data File (*.pdf);;"
        response = QFileDialog.getOpenFileNames(
            parent=self, caption="Select file(s)", dir=os.getcwd(), filter=file_filter
        )
        file_paths, _ = response

        # Save copy of files
        for file_path in file_paths:
            self.db.store_pdf(file_path)
            print(f"Sucessfully uploaded file at path: {file_path}")

        self.db.parse_pdf_to_db()
        self.db.move_pdf(
            old_path="app_storage/pdfs/to_process",
            new_path="app_storage/pdfs/processed",
        )

        self.show_reference_list(file_paths)
        self.show_conversation_frame()

    def show_reference_list(self, document_list: List[str]):
        """
        This function displays uploaded docs title on right sigh widget
        """
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

# Reload the app when a Python file changes
class ReloadHandler(FileSystemEventHandler):
    def __init__(self, app_restart_callback):
        super().__init__()
        self.app_restart_callback = app_restart_callback

    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Only watch Python files
            print(f"Detected change in {event.src_path}, restarting app...")
            self.app_restart_callback()

def restart_app():
    # Kill the current process and restart it
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

## Uncomment this code to enable auto-reloading
# if __name__ == "__main__":
#     observer = Observer()
#     handler = ReloadHandler(restart_app)
#     observer.schedule(handler, path=".", recursive=True)
#     observer.start()

#     try:
#         app = QApplication(sys.argv)
#         main_window = MainWindow()
#         main_window.show()
#         sys.exit(app.exec())
#     except KeyboardInterrupt:
#         print("Stopping watcher...")
#         observer.stop()
#     finally:
#         observer.join()
