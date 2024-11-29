import json

from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QHBoxLayout, QWidget, QSpacerItem, \
    QScrollArea

from reference_widget import ReferenceWidget


class ChatDialog(QScrollArea):
    def __init__(self, chat_data):
        super().__init__()
        # Create a widget to hold the content
        self.content_widget = QWidget()
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)
        
        self.setupUi()
        self.chats_data = chat_data
        self.show_chats()

    def setupUi(self):
        # Main vertical layout for stacking messages
        self.verticalLayout = QVBoxLayout(self.content_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Add a spacer item at the bottom to push messages upwards
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.verticalSpacer)

    def show_chats(self):
        chat_list = self.chats_data.get("chat_list", [])
        for chat in chat_list:
            input_str = chat.get("input_str")
            self.addMessage(input_str, user=True, reference_info=None)
            
            out_str = chat.get("out_str")
            reference_info = chat.get("references_info")
            self.addMessage(out_str, user=False, reference_info=reference_info)

    def addMessage(self, message, user, reference_info):
        # Create a horizontal layout for each message
        message_layout = QHBoxLayout()
        
        if user:
            # User message (right-aligned)
            message_label = QLabel(self)
            message_label.setText(message)
            message_label.setWordWrap(True)
            message_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            message_label.setStyleSheet("""
                QLabel {
                    background-color: rgba(173, 216, 230, 180);
                    border: 1px solid rgb(0, 120, 215);
                    padding: 10px;
                    border-radius: 10px;
                }
            """)
            message_label.setAlignment(Qt.AlignRight)
            message_layout.addStretch()
            message_layout.addWidget(message_label)
        else:
            # System message (left-aligned)
            response_frame = ReferenceWidget(message, reference_info)
            response_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            message_layout.addWidget(response_frame)
            message_layout.addStretch()

        # Insert the message layout before the spacer
        self.verticalLayout.insertLayout(self.verticalLayout.count() - 1, message_layout)


if __name__ == "__main__":
    pass

    # import sys
    #
    # app = QApplication(sys.argv)
    # window = ChatDialog(chat_data[0])
    # window.show()
    # sys.exit(app.exec())
