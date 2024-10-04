import sys
from PyQt6.QtWidgets import (
    QGridLayout, QMainWindow, QWidget, QApplication, QLabel
)
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(QLabel('Red'), 1, 0)
        layout.addWidget(Color('green'), 2, 0)
        layout.addWidget(QLabel('Green'), 3, 0)
        layout.addWidget(Color('blue'), 0, 1)
        layout.addWidget(QLabel('Blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)
        layout.addWidget(QLabel('Purple'), 3, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
