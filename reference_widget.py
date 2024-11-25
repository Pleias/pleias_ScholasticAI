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
             # Specify the image and TSV file paths
            image_path = "path/to/image.jpg"  # Replace with your image path
            tsv_path = "path/to/coordinates.tsv"  # Replace with your TSV path

            # Open the QScrollArea with the image and rectangle
            self.show_image_with_highlight(image_path, tsv_path)

        super().mousePressEvent(event)

    def show_image_with_highlight(self, image_path, tsv_path):
        # Read the coordinates from the TSV file
        coordinates = self.read_coordinates_from_tsv(tsv_path)
        if not coordinates:
            print("Invalid coordinates file.")
            return

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWindowTitle("Image Viewer")
        scroll_area.resize(800, 600)

        # Create a widget to display the image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image: {image_path}")
            return

        # Add the image to the label
        image_label.setPixmap(pixmap)

        # Create a custom widget to overlay the rectangle
        overlay_widget = QLabel()
        overlay_widget.setPixmap(self.add_highlight_to_pixmap(pixmap, coordinates))
        overlay_widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Set up the scroll area
        container_widget = QWidget()
        layout = QVBoxLayout(container_widget)
        layout.addWidget(overlay_widget)
        scroll_area.setWidget(container_widget)

        # Show the scroll area
        scroll_area.show()

    def read_coordinates_from_tsv(self, tsv_path):
        """Reads coordinates from a TSV file. Assumes format: x1\ty1\tx2\ty2"""
        try:
            with open(tsv_path, "r") as file:
                line = file.readline().strip()
                x1, y1, x2, y2 = map(int, line.split("\t"))
                return x1, y1, x2, y2
        except Exception as e:
            print(f"Error reading TSV file: {e}")
            return None

    def add_highlight_to_pixmap(self, pixmap, coordinates):
        """Draws a rectangle over the pixmap based on coordinates."""
        x1, y1, x2, y2 = coordinates

        # Create a painter to draw on the pixmap
        highlighted_pixmap = pixmap.copy()
        painter = QPainter(highlighted_pixmap)
        painter.setPen(QColor(255, 0, 0, 200))  # Red color with transparency
        painter.setBrush(QColor(255, 0, 0, 50))  # Transparent red fill
        painter.drawRect(x1, y1, x2 - x1, y2 - y1)
        painter.end()

        return highlighted_pixmap

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
