from PySide6.QtGui import QPixmap, Qt, QFontMetrics
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QLabel, QSizePolicy, QTextBrowser
import sys
from ui_one_reference_frame import Ui_one_reference
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView

html = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transformers Architecture</title>
    <style>
      body {
        font-family: SF Pro;
        font-size: 16px;
        font-weight: 400;
        line-height: 22px;
        letter-spacing: -0.4300000071525574px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
      }
      .marker {
        width: 16px;
        height: 18px;
        padding: 0px 2px;
        justify-content: center;
        align-items: center;
        border-radius: 3px;
      }
      .blue {
        color: #042FF4;
        font-family: SF Pro;
        font-size: 12px;
        font-style: normal;
        font-weight: 200;
        line-height: normal;
        background: #BFEFFF;
      }
      .yellow {
        color: #B66400;
        font-family: SF Pro;
        font-size: 12px;
        font-weight: 200;
        line-height: 14.32px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        background: #FFE289;
      }
    </style>
  </head>
  <body>
    <p> The primary feature of the Transformers architecture is the self-attention mechanism <span class="marker blue">1</span>. This allows the model to weigh the importance of different words in a sentence dynamically and compute relationships between them, which helps in capturing long-range dependencies and contextual information efficiently <span class="marker blue">2</span>. Transformers also use an encoder-decoder architecture and avoid sequential operations, enabling them to be parallelised more effectively than traditional models like recurrent neural networks (RNNs) <span class="marker blue">1</span>
      <span class="marker yellow">3</span>.
    </p>
  </body>
</html>
"""

square_html_yellow = """
<div style="
    display: inline-block;
    width: 16px;
    height: 18px;
    background-color: #FFE289;
    color: #B66400;
    border-radius: 3px 0px 0px 0px;
    font-size: 15px;
    text-align: center;
    font-weight: 200;
    line-height: 16px;
    opacity: 0px;
">2</div>
"""
square_html = """
<div style="
    display: inline-block;
    width: 16px;
    height: 18px;
    background-color: #BFEFFF;
    color: #042FF4;
    border-radius: 3px 0px 0px 0px;
    font-size: 15px;
    text-align: center;
    font-weight: 200;
    line-height: 16px;
    opacity: 0px;
">2</div>
"""


# app = QApplication([])
#
# web_view = QWebEngineView()
# web_view.setHtml(html)
# web_view.show()
#
# app.exec()

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
        print(self.ui.ref_number)
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

        web_view = QWebEngineView()
        web_view.setHtml(square_html)
        web_view.setMaximumSize(50, 50)

        self.ui.ref_number.setHtml(square_html_yellow)
        self.ui.ref_number.setMaximumSize(50, 50)

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

        text = """
    The primary feature of the Transformers architecture is the self-attention mechanism <span style="border: 1px solid #007bff; padding: 2px; border-radius: 3px; background-color: #e7f3ff; color: #007bff; font-size: 12px;">1</span>.
    This allows the model to weigh the importance of different words dynamically, capturing long-range dependencies efficiently
    <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span>.
    Transformers also use an encoder-decoder architecture that avoids sequential operations
     <span style="border: 1px solid #6c757d; padding: 2px; border-radius: 3px; background-color: #f1f1f1; color: #6c757d; font-size: 12px;">2</span> <span style="border: 1px solid #ffc107; padding: 2px; border-radius: 3px; background-color: #fff3cd; color: #856404; font-size: 12px;">3</span>.
    """
        label = QLabel()
        font_metrics = QFontMetrics(label.font())
        width = font_metrics.horizontalAdvance(text)
        height = font_metrics.height()
        print(f'Width: {width}, Height: {height}')

        self.layout = QVBoxLayout(self)
        web_view = QWebEngineView()
        web_view.setHtml(html)
        width_content_based = 600
        height_content_based = width // 600 * 22
        web_view.setMaximumSize(width_content_based, height_content_based)
        response_label = web_view
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
