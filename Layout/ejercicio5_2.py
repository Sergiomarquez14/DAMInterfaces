import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QStackedLayout
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
        super().__init__()

        self.setWindowTitle("Cambio de color")

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.stacked_layout = QStackedLayout()

        self.stacked_layout.addWidget(Color("red"))
        self.stacked_layout.addWidget(Color("green"))
        self.stacked_layout.addWidget(Color("blue"))
        self.stacked_layout.addWidget(Color("yellow"))

        boton_layout = QHBoxLayout()

        botonrojo = QPushButton("Red")
        botonverde = QPushButton("Green")
        botonazul = QPushButton("Blue")
        botonamarillo = QPushButton("Yellow")

        botonrojo.pressed.connect(lambda: self.cambio_color(0)) 
        botonverde.pressed.connect(lambda: self.cambio_color(1))
        botonazul.pressed.connect(lambda: self.cambio_color(2))
        botonamarillo.pressed.connect(lambda: self.cambio_color(3))

        boton_layout.addWidget(botonrojo)
        boton_layout.addWidget(botonverde)
        boton_layout.addWidget(botonazul)
        boton_layout.addWidget(botonamarillo)

        layout.addLayout(boton_layout)
        layout.addLayout(self.stacked_layout)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def cambio_color(self, index):
        self.stacked_layout.setCurrentIndex(index)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
