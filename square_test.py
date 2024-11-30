from PySide6.QtCore import QSize
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

app = QApplication([])

web_view = QWebEngineView()
web_view.setFixedSize(QSize(500, 200))
print("actual size", web_view.size())
print("size policy", web_view.sizePolicy())
print("size hint", web_view.sizeHint())
print("minimum hint", web_view.minimumSizeHint())
web_view.setHtml(html)
web_view.show()
app.exec()

