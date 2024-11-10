import json

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, \
    QScrollArea

from reference_widget import ReferenceWidget


class ChatDialog(QScrollArea):
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
            self.addMessage(input_str, user=True, reference_info=None)

            out_str = chat.get("out_str")
            reference_info = chat.get("references_info")
            self.addMessage(out_str, user=False, reference_info=reference_info)

    def addMessage(self, message, user, reference_info):
        """
        Add a message to the chat.
        - If `user` is True, it aligns the message to the right (user input).
        - If `user` is False, it aligns the message to the left (system output) and uses ResponseFrame.
        """
        # Create a horizontal layout for each message
        message_layout = QHBoxLayout()

        if user:
            # Create QLabel for the user message
            message_label = QLabel(self)
            message_label.setText(message)
            message_label.setWordWrap(True)
            message_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

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
            # System output (aligned left) using ResponseFrame
            response_frame = ReferenceWidget(message, reference_info)
            response_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            message_layout.addWidget(response_frame)
            message_layout.addStretch()  # Push the label to the left

        # Add the message layout to the main vertical layout
        self.verticalLayout.insertLayout(self.verticalLayout.count() - 1, message_layout)


if __name__ == "__main__":
    pass

    # import sys
    #
    # app = QApplication(sys.argv)
    # window = ChatDialog(chat_data[0])
    # window.show()
    # sys.exit(app.exec())
