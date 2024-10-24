import sys
from PyQt6 import QtWidgets, uic

class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    def __init__(self, padre=None):
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("dosbotones.ui", self)
        
        self.setWindowTitle("Ejemplo") 

        self.pushButton.clicked.connect(self.funcion)
        self.pushButton_2.clicked.connect(self.auto)

    def funcion(self):
        if self.progressBar.value() > self.progressBar.minimum():
            self.progressBar.setValue(self.progressBar.value() - 5)
        else:
            self.progressBar.setValue(100)
    
    def auto (self):
        if self.label.text() == "Benito":
            self.label.setText("Dandy")
            self.label.setStyleSheet("color: red;")
        else:
            self.label.setText("Benito")
            self.label.setStyleSheet("color: black;")

    
app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
sys.exit(app.exec())
