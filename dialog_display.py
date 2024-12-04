from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSpacerItem,
    QScrollArea,
)

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
        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )
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
                    background-color: #F2F2F2;
                    border: 1px solid #E0E0E0;
                    padding: 8px;
                    border-radius: 8px;
                }
            """)
            message_label.setAlignment(Qt.AlignRight)
            message_layout.addStretch()
            message_layout.addWidget(message_label)
        else:
            response_frame = ReferenceWidget(message, reference_info)
            response_frame.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            message_layout.addWidget(response_frame)
            message_layout.addStretch()

        self.verticalLayout.insertLayout(
            self.verticalLayout.count() - 1, message_layout
        )
