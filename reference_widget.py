from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QLabel
import sys
from ui_one_reference_frame import Ui_one_reference


class OneReferenceFrame(QFrame):
    def __init__(self,
                 new_ref_numer: int = 1,
                 source_icon_local: bool = True,
                 title: str = None,
                 author: list = None,
                 source_database: str = 'local',
                 creation_date: str = None,
                 ):
        super().__init__()
        self.ui = Ui_one_reference()
        self.ui.setupUi(self)
        """
        This widget is one reference entry displayed under each output msg. It includes the next fields:
        :param new_ref_numer: could be only '1', '2', '3' as soon as we provide only 3 references per answer
        :param source_icon_local: we have to types of icons local and global for OpenAlex and Archive
        :param title: this is a paper title
        :param author: this is a paper authors plus year
        :param source_database: this field is empty if we don't use OpenAlex or Archive etc. Otherwise, database icon
        :return: None
        """
        self.ui.ref_number.setText(new_ref_numer)

        if source_icon_local:
            self.ui.ref_start_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        else:
            self.ui.ref_start_icon.setPixmap(QPixmap(u"static/icons/icon_web.svg"))

        title = title if len(title) else "No paper title identified"
        author = author if len(author) else "No paper author identified"
        self.ui.ref_paper_title.setText(title)
        self.ui.ref_authors.setText(author)
        if source_database == "local":
            self.ui.ref_last_icon.clear()
            self.ui.ref_text.setText("")
        elif source_database == "open_alex":
            self.ui.ref_last_icon.setPixmap(QPixmap(u"static/icons/logo_openalex.png"))
            pass
        elif source_database == "archive":
            self.ui.ref_last_icon.setPixmap(QPixmap(u"static/icons/archive.svg"))
            self.ui.ref_text.setText("")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet("background-color: lightgray;")
            print("Frame clicked!")  # Handle frame click here
        super().mousePressEvent(event)

    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.setStyleSheet(f"background-color: (255, 255, 255);")  # Reset color on release
    #     super().mouseReleaseEvent(event)


class ReferenceWidget(QWidget):
    def __init__(self, html_response, references_info):
        super().__init__()
        self.layout = QVBoxLayout(self)
        response_label = QLabel()
        response_label.setText(html_response)
        response_label.setWordWrap(True)
        self.layout.addWidget(response_label)

        for i, reference_info in enumerate(references_info):
            reference_info['new_ref_numer'] = str(i + 1)
            reference = OneReferenceFrame(**reference_info)
            self.layout.addWidget(reference)


if __name__ == "__main__":
    example_local = {
        'new_ref_numer': '1',
        'source_icon_local': True,
        'title': 'Paper Title found on Local database',
        'author': 'Authors info found on Local database',
        'source_database': 'local',
    }

    example_open_alex = {
        'new_ref_numer': '2',
        'source_icon_local': False,
        'title': 'Paper Title found on Open Alex',
        'author': 'Authors info found on Open Alex',
        'source_database': 'open_alex',
    }
    example_archive = {
        'new_ref_numer': '3',
        'source_icon_local': False,
        'title': 'Paper Title found on archive',
        'author': 'Authors info found on archive',
        'source_database': 'archive',
    }
    html_response = """
    The primary feature of the Transformers architecture is the self-attention mechanism <span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">1</span>.
    This allows the model to weigh the importance of different words dynamically, capturing long-range dependencies efficiently
    <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span>.
    Transformers also use an encoder-decoder architecture that avoids sequential operations
     <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span> <span style="border: 1px solid #ffc107; padding: 2px; border-radius: 3px; background-color: #fff3cd; color: #856404; font-size: 12px;">3</span>.
    """
    references_info = [example_local, example_archive, example_open_alex]
    app = QApplication(sys.argv)
    window = ReferenceWidget(html_response, references_info)
    window.show()
    sys.exit(app.exec())
