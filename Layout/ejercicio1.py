import sys
from PyQt6.QtWidgets import (
    QVBoxLayout, QMainWindow, QWidget, QApplication, QPushButton, QLineEdit
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


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

        layout = QVBoxLayout()

        layout.addWidget(QPushButton("Este es un ejemplo de boton"))
        layout.addWidget(QLineEdit("Este es un ejemplo de LineEdit"))
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
