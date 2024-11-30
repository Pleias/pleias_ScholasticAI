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
    import sys
    chat_data = {
    "title": "Hi",
    "chat_list": [
      {
        "input_str": "Hi",
        "out_str": "\n\nThe query pertains to technical work performed in the field of computer science, specifically focusing on research conducted while at Google Research. The reference **7b3a9c2d4e8f5g1h** provides a detailed description of this work. It states that the work was performed while the individual was affiliated with Google Research<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">1</span>.\n\nThe provided reference **DB-2023-001** does not offer additional context beyond the URL it contains. It does not provide any further relevant information for the query, focusing solely on the database entry itself<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">2</span>. Therefore, **DB-2023-001** can be excluded from the answer.\n\nIn conclusion, the most pertinent information for the query is found in **7b3a9c2d4e8f5g1h**, which directly addresses the work performed at Google Research.",
        "references_info": [
          {
            "title": "",
            "author": "",
            "creation_date": "2024-04-10"
          }
        ]
      },
      {
        "input_str": "transformers",
        "out_str": "\n\nTransformers are advanced neural network models that have revolutionized natural language processing (NLP) and machine translation (MT). They are known for their ability to perform unsupervised multitask learning, which allows them to learn multiple tasks simultaneously, enhancing their overall performance in various NLP applications<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">1</span>.\n\nTransformers excel at character-level language modeling, which involves predicting the next character in a sequence of text. This capability is crucial for tasks such as generating coherent and meaningful text, as demonstrated by models like BERT and GPT-2<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">1</span>.\n\nIn the context of machine translation, transformers have shown significant improvements over traditional approaches. They can be trained on large amounts of parallel data, which is not always available for some languages, making them effective even in low-resource settings<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">1</span>. The ability of transformers to perform end-to-end translation without any need for alignment or segmentation makes them particularly efficient<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">2</span>.\n\nFurthermore, transformers have been applied to other NLP tasks such as image captioning, where they can generate natural language descriptions from visual inputs. This capability is crucial for applications in computer vision and natural language interaction<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">2</span>.\n\nThe robustness of transformers to various challenges has also been highlighted. They can handle strange poses in images, which can be a significant improvement over traditional methods that are easily fooled by such variations<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">2</span>. Additionally, transformers are pre-trained on large corpora to enhance their ability to understand and generate human language, making them a valuable tool for tasks like question answering and conversational agents<span style=\"border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;\">2</span>.\n\nIn summary, transformers are versatile models that excel in a wide range of NLP tasks due to their ability to perform unsupervised multitask learning, their effectiveness in character-level language modeling, and their application in high-precision machine translation and other complex NLP tasks.",
        "references_info": [
          {
            "title": "Language Models are Unsupervised Multitask Learners",
            "author": "Alec Radford*, Jeffrey Wu*, Rewon Child, David Luan, Dario Amodei**, Ilya Sutskever**",
            "creation_date": "2019-02-14"
          },
          {
            "title": "",
            "author": "",
            "creation_date": "2024-04-10"
          }
        ]
      }
    ]
  }
    app = QApplication(sys.argv)
    window = ChatDialog(chat_data)
    window.show()
    sys.exit(app.exec())
