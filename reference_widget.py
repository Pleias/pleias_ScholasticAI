from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout
import sys
from ui_one_reference_frame import Ui_one_reference


class OneReferenceFrame(QFrame):
    def __init__(self,
                 new_ref_numer: str = None,
                 source_icon_local: bool = True,
                 source_title: str = None,
                 source_authors: list = None,
                 source_database: str = 'local',
                 ):
        super().__init__()
        self.ui = Ui_one_reference()
        self.ui.setupUi(self)
        """
        This widget is one reference entry displayed under each output msg. It includes the next fields:
        :param new_ref_numer: could be only '1', '2', '3' as soon as we provide only 3 references per answer
        :param source_icon_local: we have to types of icons local and global for OpenAlex and Archive
        :param source_title: this is a paper title
        :param source_authors: this is a paper authors plus year
        :param source_database: this field is empty if we don't use OpenAlex or Archive etc. Otherwise, database icon
        :return: None
        """

        self.ui.ref_number.setText(new_ref_numer)

        if source_icon_local:
            self.ui.ref_start_icon.setPixmap(QPixmap(u"static/icons/icons8-document-ios-17-outlined-50.png"))
        else:
            self.ui.ref_start_icon.setPixmap(QPixmap(u"static/icons/icon_web.svg"))
        self.ui.ref_paper_title.setText(source_title)
        self.ui.ref_authors.setText(source_authors)
        if source_database == "local":
            self.ui.ref_last_icon.clear()
            self.ui.ref_text.setText("")
        elif source_database == "open_alex":
            "Do nothing as OpenAlex is used as a default icon"
            pass
        elif source_database == "archive":
            self.ui.ref_last_icon.setPixmap(QPixmap(u"static/icons/archive.svg"))
            self.ui.ref_text.setText("")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet("background-color: lightgray;")
            print("Frame clicked!")  # Handle frame click here
        super().mousePressEvent(event)


class ReferenceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        example_local = {
            'new_ref_numer': '1',
            'source_icon_local': True,
            'source_title': 'Paper Title found on Local database',
            'source_authors': 'Authors info found on Local database',
            'source_database': 'local',
        }

        example_open_alex = {
            'new_ref_numer': '2',
            'source_icon_local': False,
            'source_title': 'Paper Title found on Open Alex',
            'source_authors': 'Authors info found on Open Alex',
            'source_database': 'open_alex',
        }
        example_archive = {
            'new_ref_numer': '3',
            'source_icon_local': False,
            'source_title': 'Paper Title found on archive',
            'source_authors': 'Authors info found on archive',
            'source_database': 'archive',
        }
        reference = OneReferenceFrame(**example_local)
        reference1 = OneReferenceFrame(**example_open_alex)
        reference2 = OneReferenceFrame(**example_archive)
        self.layout.addWidget(reference)
        self.layout.addWidget(reference1)
        self.layout.addWidget(reference2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReferenceWidget()
    window.show()
    sys.exit(app.exec())