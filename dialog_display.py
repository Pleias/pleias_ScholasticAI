import json

from PySide6.QtCore import (QCoreApplication, Qt)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget)


class ChatDialog(QWidget):
    def __init__(self, index=0):
        super().__init__()
        self.setupUi()
        with open('data.json', 'r') as f:
            self.chats_data = json.load(f)[index]
        self.show_chats()

    def setupUi(self):
        # Set up the window properties
        self.setWindowTitle(QCoreApplication.translate("Form", "Chat Dialog"))
        # Main vertical layout for stacking messages
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

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
        message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

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
        self.verticalLayout.addLayout(message_layout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = ChatDialog()
    window.show()
    sys.exit(app.exec())
