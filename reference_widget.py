from PySide6.QtGui import QPixmap, Qt, QPainter, QColor
from PySide6.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout, QLabel, QScrollArea, QDialog
import sys
from ui_one_reference_frame import Ui_one_reference
import sqlite3
import sqlite_vec
import ast


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
        painter.setPen(QColor(100,220,240,255))  # Red color with transparency
        painter.setBrush(QColor(100,220,240,100))  # Transparent red fill
        painter.drawRect(x1, y1, x2 - x1, y2 - y1)
        painter.end()

        return highlighted_pixmap


class OneReferenceFrame(QFrame):
    def __init__(self,
                 new_ref_number: int = 1,
                 source_icon_local: bool = True,
                 document_id: int = None,
                 chunk_id : int = None,
                 title: str = None,
                 author: list = None,
                 source_database: str = 'local',
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
        self.ui.ref_number.setText(new_ref_number)

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
        
         # Fetch metadata for this instance
            self.doc_metadata, self.chunk_metadata = self.fetch_metadata()
            if self.doc_metadata:
                print(f"Fetched metadata for document_id {self.document_id}: {self.doc_metadata}")
            if self.chunk_metadata:
                print(f"Fetched metadata for chunk_id {self.chunk_id}: {self.chunk_metadata}")

        elif source_database == "open_alex":
            self.ui.ref_last_icon.setPixmap(QPixmap("static/icons/logo_openalex.png"))
            pass
            
        elif source_database == "archive":
            self.ui.ref_last_icon.setPixmap(QPixmap("static/icons/archive.svg"))
            self.ui.ref_text.setText("")

    
    def fetch_metadata(self):
        """Fetch metadata for the current document_id from the database."""
        if self.document_id is None:
            print("Document ID is not set.")
            return None

        try:
            # Connect to the database
            connection = sqlite3.connect("app_storage/metadata/sqlite-poc.db")
            
            # Query the pdf_metadata table for the row with id = self.document_id
            cursor = connection.cursor()

            ##### DOC METADATA
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
            

            ##### CHUNK METADATA
            query = "SELECT * FROM chunks WHERE document_id = ? AND chunk_id = ?"
            cursor.execute(query, (self.document_id, self.chunk_id))
            row = cursor.fetchone()

            if row:
                # Convert row into a dictionary
                columns = [description[0] for description in cursor.description]
                chunk_metadata = dict(zip(columns, row))
            else:
                print(f"No chunk data found for document_id: {self.document_id} and chunk_id: {self.chunk_id}")
                return None
            return doc_metadata, chunk_metadata
            
            

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            connection.close()



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.setStyleSheet("background-color: lightgray;")
            """
            print(vars(self))
            print("Frame clicked!")  # Handle frame click here
            print("new ref number ", self.new_ref_number)
            print("doc id ",self.document_id)
            print("chunk id ",self.chunk_id)
            print("title ",self.title)
            print("author" ,self.author)
            print("source database ",self.source_database)
            print("creation date ",self.creation_date)
            """
            # Specify the image and TSV file paths
            doc_filename = self.doc_metadata["file_name"]
            page_number = ast.literal_eval(self.chunk_metadata["pages"])[0] #☻Retrieving the first page if there are more than one
            image_path = f"temp/intermediate_folders/{doc_filename}_output/{doc_filename}_images/{doc_filename}_page{page_number}.jpg"  
           
            json_path = f"temp/intermediate_folders/{doc_filename}_output/final/{doc_filename}.json"

            # Open the QScrollArea with the image and rectangle
            self.show_image_with_highlight(image_path, json_path)

            

        super().mousePressEvent(event)

    def show_image_with_highlight(self, image_path, json_path):
        # Read the coordinates from the TSV file
        coordinates = (0, 0, 100, 100)  # Example coordinates for testing
        #coordinates = (58.07,140.55700000000002,536.32,595.65)
        #### COORDINATES FROM JSON PATH
        if not coordinates:
            print("Invalid coordinates file.")
            return

        # Open a new ReferenceViewer window
        viewer = ReferenceViewer(image_path, coordinates)
        viewer.exec()  # Use exec() to display the dialog modally


    


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
            reference_info['new_ref_number'] = str(i + 1)
            reference = OneReferenceFrame(**reference_info)
            self.layout.addWidget(reference)


if __name__ == "__main__":
    example_local = {
        'new_ref_number': '1',
        'source_icon_local': True,
        'title': 'Paper Title found on Local database',
        'author': 'Authors info found on Local database',
        'source_database': 'local',
    }

    example_open_alex = {
        'new_ref_number': '2',
        'source_icon_local': False,
        'title': 'Paper Title found on Open Alex',
        'author': 'Authors info found on Open Alex',
        'source_database': 'open_alex',
    }
    example_archive = {
        'new_ref_number': '3',
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
