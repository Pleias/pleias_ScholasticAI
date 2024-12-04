from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget


class FileManagementWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("File Management")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # File list to display the files added by the user
        self.file_list = QListWidget(self)
        layout.addWidget(self.file_list)

        # Button to add a new file
        self.add_file_button = QPushButton("Add File", self)
        layout.addWidget(self.add_file_button)

        # Connect the button to the file upload functionality
        self.add_file_button.clicked.connect(self.add_file)

    def add_file(self):
        # Open a file dialog to select a file
        file_name, _ = QFileDialog.getOpenFileName(self, "Add File", "", "All Files (*)")
        if file_name:
            # Add the selected file to the list
            self.file_list.addItem(file_name)
