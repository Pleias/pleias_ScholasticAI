import sys
from PySide6.QtCore import QStringListModel, QModelIndex, Qt
from dialog_display import ChatDialog
from ui_froms.ui_main_window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea
from get_answer_from_api import get_response
from connect_db import ConnectDB


# 1. если начали новый чат и ничего не кликнули то каждый раз когда юзер пишет доп сообщение, получается что создается новый чат;
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect_db = ConnectDB()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show_chat_list()
        self.ui.send_message_btn.clicked.connect(self.get_response)  # Send msg botton
        self.ui.chat_list.clicked.connect(self.on_item_clicked)  # Click on existing dialog

    def on_item_clicked(self, index: QModelIndex):
        """
        This function display the dialog if users clicks on it
        """
        # Get the row number from the QModelIndex
        row = index.row()
        self.chat_dialog = ChatDialog(index=row)
        self.ui.scrollArea.setWidget(self.chat_dialog)
        self.ui.message_input.clear()

    def show_chat_list(self):
        chat_list = self.connect_db.get_chat_title_list()
        self.model = QStringListModel(chat_list)
        self.ui.chat_list.setModel(self.model)

    def get_response(self):
        chat_db = self.connect_db.get_chat_data()  # [{}{}]
        message_input = self.ui.message_input.toPlainText().strip()
        response_str = get_response(message_input)

        # How to continue existing chat
        if self.ui.chat_list.selectedIndexes():
            print("Am here ")
            # Get current selected chat index
            current_index = self.ui.chat_list.currentIndex()
            select_row = current_index.row()
            chat_db[select_row]["chat_list"] += [{"input_str": message_input, "out_str": response_str}]
            self.connect_db.save_chat_data(chat_db)

        # How to create new chat
        else:
            chat_data = {
                "title": message_input,
                "chat_list": [{"input_str": message_input, "out_str": response_str}]}
            # Update database
            chat_db.insert(1, chat_data)
            self.connect_db.save_chat_data(chat_db)
            self.ui.chat_list.setCurrentIndex(self.model.index(1))
            print(f"Set current index to: {self.model.index(1).row()}")

        index = self.ui.chat_list.currentIndex().row()
        print("-" * 100)
        print(f"The next msg will go to the dialog index: {index}")
        print(f"\n\n{self.ui.chat_list.selectedIndexes()} - this is out if \n\n")
        dialog = ChatDialog(index=index)
        self.ui.scrollArea.setWidget(dialog)
        self.ui.message_input.clear()
        self.show_chat_list()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
