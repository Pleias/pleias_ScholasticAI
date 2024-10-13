from PySide6.QtWidgets import QListView, QMainWindow, QApplication, QVBoxLayout, QWidget, QTextEdit, QPushButton
from PySide6.QtCore import QStringListModel, QModelIndex, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QWidget to hold the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create ListView for the dialog list
        self.list_view = QListView(self)

        # Example data for the ListView (dialogs)
        self.dialog_list = ["Dialog 1: Hello!", "Dialog 2: How can I help you?", "Dialog 3: Thank you!"]

        # Model holding the dialog data
        self.model = QStringListModel(self.dialog_list)

        # Set model to the ListView
        self.list_view.setModel(self.model)

        # Create a QTextEdit to display the dialog content
        self.dialog_display = QTextEdit(self)
        self.dialog_display.setReadOnly(True)  # Make it read-only

        # Create a button to set a specific index (e.g., the second item)
        self.set_index_button = QPushButton("Set Index to 2", self)
        self.set_index_button.clicked.connect(self.set_current_index_to_second_item)

        # Create a layout and add widgets
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.list_view)
        layout.addWidget(self.dialog_display)
        layout.addWidget(self.set_index_button)

        # Connect the clicked signal to the slot (function)
        self.list_view.clicked.connect(self.on_item_clicked)

    def on_item_clicked(self, index: QModelIndex):
        # Get the row number from the QModelIndex when an item is clicked
        row = index.row()

        # Log the clicked item and row for reference
        print(f"User clicked on: '{self.model.data(index, Qt.ItemDataRole.DisplayRole)}', at index: {row}")

        # Load the dialog by index and display it
        dialog_content = self.load_dialog_by_index(row)
        self.dialog_display.setPlainText(dialog_content)

    def set_current_index_to_second_item(self):
        # Set the current index to the second item in the list (index 1)
        index = self.model.index(1)  # Get QModelIndex for row 1
        if index.isValid():
            self.list_view.setCurrentIndex(index)  # Set it as the current index
            print(f"Set current index to: {index.row()}")

            # Optionally, display the dialog content
            dialog_content = self.load_dialog_by_index(index.row())
            self.dialog_display.setPlainText(dialog_content)

    def load_dialog_by_index(self, index: int):
        """
        Simulate loading a dialog by its index.
        """
        if 0 <= index < len(self.dialog_list):
            return self.dialog_list[index]
        else:
            return "Dialog not found."


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
