import json

from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem)


class ChatDialog(QWidget):
    """
    Take in chat data dict and displays it
    """

    def __init__(self, chat_data):
        super().__init__()
        self.setupUi()
        self.chats_data = chat_data
        self.show_chats()

    def setupUi(self):
        # Set up the window properties
        self.setWindowTitle(QCoreApplication.translate("Form", "Chat Dialog"))

        # Main vertical layout for stacking messages
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Add a spacer item at the bottom to push messages upwards
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

    def show_chats(self):
        chat_list = self.chats_data.get("chat_list")
        for chat in chat_list:
            input_str = chat.get("input_str")
            self.addMessage(input_str, user=True)

            out_str = chat.get("out_str")
            self.addMessage(out_str, user=False)

    def addMessage(self, message, user):
        """
        Add a message to the chat.
        - If `user` is True, it aligns the message to the right (user input).
        - If `user` is False, it aligns the message to the left (system output).
        """
        # Create a horizontal layout for each message
        message_layout = QHBoxLayout()

        # Create QLabel for the message
        message_label = QLabel(self)
        message_label.setText(message)
        message_label.setWordWrap(True)  # Allow text to wrap

        # Set a size policy to prevent unnecessary expansion
        message_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

        if user:
            # User input (aligned right)
            message_label.setStyleSheet("""
                background-color: rgba(173, 216, 230, 180);  /* Light blue background */
                border: 1px solid rgb(0, 120, 215);          /* Border */
                padding: 10px;                               /* Padding */
                border-radius: 10px;                         /* Rounded corners */
            """)
            message_label.setAlignment(Qt.AlignRight)  # Align text to the right
            message_layout.addStretch()  # Push the label to the right
            message_layout.addWidget(message_label)
        else:
            # System output (aligned left)
            message_label.setStyleSheet("""
                background-color: rgba(240, 240, 240, 180);  /* Light gray background */
                border: 1px solid rgb(180, 180, 180);         /* Border */
                padding: 10px;                                /* Padding */
                border-radius: 10px;                          /* Rounded corners */
            """)
            message_label.setAlignment(Qt.AlignLeft)  # Align text to the left
            message_layout.addWidget(message_label)
            message_layout.addStretch()  # Push the label to the left

        # Add the message layout to the main vertical layout
        self.verticalLayout.insertLayout(self.verticalLayout.count() - 1, message_layout)


if __name__ == "__main__":
    import sys
    chat_data = [{"title": "Hi, how are you?", "chat_list": [{"input_str": "Hi, how are you?", "out_str": "16 This is model answer"}, {"input_str": "Good and you?", "out_str": "13 This is model answer"}, {"input_str": "Dark is a dark appearance that doesn\u2019t change. Dark Mode darkens the colour scheme so the content you\u2019re working on stands out, while windows and controls seem to recede into the background. It\u2019s effective for viewing documents, presentations, photos, films, web pages and more.", "out_str": "278 This is model answer"}]}]
    app = QApplication(sys.argv)
    window = ChatDialog(chat_data[0])
    window.show()
    sys.exit(app.exec())
