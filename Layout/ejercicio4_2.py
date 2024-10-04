import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton
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

        self.setWindowTitle("Vertical and Horizontal Layout Example")

        central_widget = QWidget()
        layout = QVBoxLayout()

        boton_layout = QHBoxLayout()

        boton1 = QPushButton("Boton 1")
        boton2 = QPushButton("Boton 2")
        boton3 = QPushButton("Boton 3")

        boton_layout.addWidget(boton1)
        boton_layout.addWidget(boton2)
        boton_layout.addWidget(boton3)

        color_widget = Color('lightblue')

        layout.addLayout(boton_layout)
        layout.addWidget(color_widget)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
