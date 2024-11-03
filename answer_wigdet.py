import sys

from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QApplication
from PySide6.QtCore import Qt
from reference_widget import ReferenceWidget


class ResponseFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the frame style
        self.setStyleSheet("background-color: white; border: none; padding: 10px;")
        self.setLayout(QVBoxLayout())

        # Main response text with inline references
        response_label = QLabel()
        response_label.setText(self.generate_response_text())
        response_label.setWordWrap(True)
        self.layout().addWidget(response_label)

        # References list below the main response
        reference_widget = ReferenceWidget()
        self.layout().addWidget(reference_widget)

    def generate_response_text(self):
        # Main response text with inline reference numbers
        text = """
        The primary feature of the Transformers architecture is the self-attention mechanism <span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">1</span>.
        This allows the model to weigh the importance of different words dynamically, capturing long-range dependencies efficiently
        <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span>.
        Transformers also use an encoder-decoder architecture that avoids sequential operations
        <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span> <span style="border: 1px solid #ffc107; padding: 2px; border-radius: 3px; background-color: #fff3cd; color: #856404; font-size: 12px;">3</span>.
        """
        return text

    def generate_references_list(self):
        # Styled HTML text for the references list
        references = """
        <h3>References</h3>
        <p><span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">1</span>
        Attention is All You Need. <i>2017 Ashish Vaswani, Noam Shazeer et al.</i></p>

        <p><span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span>
        An Introduction to Transformers. <i>2018</i></p>

        <p><span style="border: 1px solid #ffc107; padding: 2px; border-radius: 3px; background-color: #fff3cd; color: #856404; font-size: 12px;">3</span>
        Transformer Machine Learning Model for Auto-Alignment. <i>2019 Qiang Wang, Bei Li et al.</i></p>
        """
        return references


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ResponseFrame()
    widget.show()
    sys.exit(app.exec_())
