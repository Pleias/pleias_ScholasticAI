from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the layout
        layout = QVBoxLayout()

        # Create a QLabel
        label = QLabel(self)

        # HTML content with inline SVG icon
        html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aligned Content</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            display: flex;
            flex-direction: column;
            margin: 10px;
        }
        .title-row {
            display: flex;
            align-items: center;
        }
        .icon {
            width: 20px;
            height: 20px;
            margin-right: 10px;
        }
        .title {
            font-family: "SF Pro", sans-serif;
            font-size: 14px;
            font-weight: 400;
            line-height: 22px;
            letter-spacing: -0.43px;
            text-align: left;
            text-underline-position: from-font;
            text-decoration-skip-ink: none;
        }
        .authors {
            margin-left: 30px;
            font-family: "SF Pro", sans-serif;
            font-size: 12px;
            font-weight: 400;
            line-height: 14.32px;
            text-align: left;
            text-underline-position: from-font;
            text-decoration-skip-ink: none;
            color: #828282;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title-row">
            <img src="icon.png" alt="Icon" class="icon">
            <span class="title">Attention is All You Need</span>
        </div>
        <div class="authors">Ashish Vaswani, Noam Shazeer et al.</div>
    </div>
</body>
</html>
'''

        # Set the HTML content to the label
        label.setText(html_content)
        label.setAlignment(Qt.AlignTop)

        # Add label to layout
        layout.addWidget(label)

        # Set the layout for the QWidget
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("HTML in QLabel with SVG Example")
        self.resize(400, 200)

# Main function to run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
