import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel(self)
        pixmap = QPixmap('madrid.jpg')
        label.setPixmap(pixmap)

        self.resize(pixmap.width(),pixmap.height())
        self.setWindowTitle("Hala Madrid")
        self.setCentralWidget(label)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

