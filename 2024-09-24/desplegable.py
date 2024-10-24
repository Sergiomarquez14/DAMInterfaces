import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        desplegable = QComboBox()
        self.setCentralWidget(desplegable)

        desplegable.addItems(["Opción 1", "Opción 2", "Opción 3"])

        desplegable.currentIndexChanged.connect(self.index_changed)
        desplegable.currentTextChanged.connect( self.text_changed )

    def index_changed(self, index):
        print(f"Índice seleccionado: {index}")
    
    def text_changed(self, text):
        print(f"Texto seleccionado: {text}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
