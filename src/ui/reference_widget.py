from PySide6.QtGui import QPixmap, Qt, QPainter, QColor, QFontMetrics
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel, QScrollArea, QDialog
from src.core.get_answer_from_api import get_html, get_title_html, get_author_html
from ui_forms.ui_one_reference_frame import Ui_Frame as Ui_one_reference
from src.core.connect_db import ConnectDB
import sqlite3
import ast


def get_square(number=1):
    return f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Square</title>
    <style>
        /* Full viewport height and centering */
        body, html {{
            height: 100%;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: white; /* Changed background to white */
        }}

        /* Square with text inside */
        .square {{
            width: 16px; /* You can adjust this */
            height: 18px; /* You can adjust this */
            background-color: #BFEFFF;
            color: #042FF4;
            border-radius: 3px; /* Rounded corners */
            font-size: 12px;
            text-align: center;
            font-weight: 590;
            line-height: 18px; /* Centers the number vertically */
        }}
    </style>
</head>
<body>

    <!-- Displaying the square with the number 2 inside -->
    <div class="square">{number}</div>
</body>
</html> 
    """


class ReferenceViewer(QDialog):
    def __init__(self, image_path, coordinates, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Reference Viewer")
        self.resize(700, 900)

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget to display the image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image: {image_path}")
            return

        # Overlay the rectangle on the image
        highlighted_pixmap = self.add_highlight_to_pixmap(pixmap, coordinates)
        image_label.setPixmap(highlighted_pixmap)
        image_label.setAlignment(Qt.AlignCenter)

        # Set up the scroll area
        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        layout.addWidget(image_label)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        layout.setSpacing(0)  # Remove spacing between widgets
        scroll_area.setWidget(container_widget)

        # Main layout for the dialog
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

    def add_highlight_to_pixmap(self, pixmap, coordinates):
        """Draws a rectangle over the pixmap based on coordinates."""
        x1, y1, x2, y2 = coordinates

        # Create a painter to draw on the pixmap
        highlighted_pixmap = pixmap.copy()
        painter = QPainter(highlighted_pixmap)
        painter.setPen(QColor(100, 220, 240, 255))  # Red color with transparency
        painter.setBrush(QColor(100, 220, 240, 100))  # Transparent red fill
        painter.drawRect(x1, y1, x2 - x1, y2 - y1)
        painter.end()

        return highlighted_pixmap


class OneReferenceFrame(QFrame):
    def __init__(
        self,
        new_ref_number: int = 1,
        source_icon_local: bool = True,
        document_id: int = None,
        chunk_id: int = None,
        title: str = None,
        author: list = None,
        source_database: str = "local",
        creation_date: str = None,
    ):
        super().__init__()
        self.ui = Ui_one_reference()
        self.ui.setupUi(self)

        # Set instance attributes
        self.new_ref_number = new_ref_number
        self.document_id = document_id
        self.chunk_id = chunk_id
        self.title = title
        self.author = author
        self.source_database = source_database
        self.creation_date = creation_date

        """
        This widget is one reference entry displayed under each output msg. It includes the next fields:
        :param new_ref_number: could be only '1', '2', '3' as soon as we provide only 3 references per answer
        :param source_icon_local: we have to types of icons local and global for OpenAlex and Archive
        :param title: this is a paper title
        :param author: this is a paper authors plus year
        :param source_database: this field is empty if we don't use OpenAlex or Archive etc. Otherwise, database icon
        :return: None
        """
        if source_icon_local:
            self.ui.doc_icon.setPixmap(
                QPixmap("static/icons/icons8-document-ios-17-outlined-50.png")
            )
        else:
            self.ui.doc_icon.setPixmap(QPixmap("static/icons/icon_web.svg"))
        title = title if len(title) else "No paper title identified"
        author = author if len(author) else "No paper author identified"

        title = get_title_html(title)
        author = get_author_html(author)
        self.ui.titles.setText(title)
        self.ui.authors.setText(author)
        square = get_square(number=int(new_ref_number))
        self.ui.webEngineView.setHtml(square)
        if source_database == "local":
            self.ui.label_2.clear()
            self.doc_metadata, self.chunk_metadata = self.fetch_metadata()
            if self.doc_metadata:
                print(
                    f"Fetched metadata for document_id {self.document_id}: {self.doc_metadata}"
                )
            if self.chunk_metadata is not None:
                print(
                    f"Fetched metadata for chunk_id {self.chunk_id}: {self.chunk_metadata}"
                )

        elif source_database == "open_alex":
            self.ui.label_2.setPixmap(QPixmap("static/icons/logo_openalex.png"))
            pass
        elif source_database == "archive":
            self.ui.label_2.setPixmap(QPixmap("static/icons/archive.svg"))

    def fetch_metadata(self):
        """Fetch metadata for the current document_id from the database."""
        if self.document_id is None:
            print("Document ID is not set.")
            return None
        connection = None
        try:
            # Connect to the database
            connection = ConnectDB().connection

            # Query the pdf_metadata table for the row with id = self.document_id
            cursor = connection.cursor()

            # DOC METADATA
            query = "SELECT * FROM pdf_metadata WHERE id = ?"
            cursor.execute(query, (self.document_id,))

            # Fetch the result
            row = cursor.fetchone()
            if row:
                # Convert the row into a dictionary for easier access
                columns = [description[0] for description in cursor.description]
                doc_metadata = dict(zip(columns, row))
            else:
                print(f"No metadata found for document_id: {self.document_id}")
                return None

            # CHUNK METADATA
            query = "SELECT * FROM chunks WHERE document_id = ? AND chunk_id = ?"
            cursor.execute(query, (self.document_id, self.chunk_id))
            row = cursor.fetchone()

            if row:
                # Convert row into a dictionary
                columns = [description[0] for description in cursor.description]
                chunk_metadata = dict(zip(columns, row))
            else:
                print(
                    f"No chunk data found for document_id: {self.document_id} and chunk_id: {self.chunk_id}"
                )
                return None
            return doc_metadata, chunk_metadata

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            if connection:
                connection.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setStyleSheet("background-color: lightgray;")
            # Specify the image and TSV file paths
            doc_filename = self.doc_metadata["file_name"]
            page_number = ast.literal_eval(self.chunk_metadata["pages"])[0]
            image_path = f"temp/intermediate_folders/{doc_filename}_output/{doc_filename}_images/{doc_filename}_page{page_number}.jpg"
            json_path = f"temp/intermediate_folders/{doc_filename}_output/final/{doc_filename}.json"

            # Open the QScrollArea with the image and rectangle
            self.show_image_with_highlight(image_path, json_path)

        super().mousePressEvent(event)

    def show_image_with_highlight(self, image_path, json_path):
        coordinates = (0, 0, 100, 100)
        if not coordinates:
            print("Invalid coordinates file.")
            return
        viewer = ReferenceViewer(image_path, coordinates)
        viewer.exec()  # Use exec() to display the dialog modally


class ReferenceWidget(QWidget):
    def __init__(self, html_response, references_info):
        super().__init__()
        label = QLabel()
        font_metrics = QFontMetrics(label.font())
        width = font_metrics.horizontalAdvance(html_response)
        self.layout = QVBoxLayout(self)
        web_view = QWebEngineView()
        html = get_html(html_response)
        web_view.setHtml(html)
        width_content_based = 600
        height_content_based = width // width_content_based * 22
        web_view.setMaximumSize(width_content_based, height_content_based)
        response_label = web_view
        self.layout.addWidget(response_label)
        for i, reference_info in enumerate(references_info):
            reference_info["new_ref_number"] = str(i + 1)
            reference = OneReferenceFrame(**reference_info)
            self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.layout.addWidget(reference)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
