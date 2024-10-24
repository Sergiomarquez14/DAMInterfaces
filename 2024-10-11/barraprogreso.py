import sys
import time
from PyQt6 import QtWidgets, uic

class Ventana(QtWidgets.QMainWindow):
    '''Esta es la clase principal'''
    # Inicializamos la ventana y conectamos los botones
    def __init__(self, padre=None):
        # Inicializa la ventana
        QtWidgets.QMainWindow.__init__(self, padre)
        uic.loadUi("barraprogreso.ui", self)  # Cargar el archivo de QtDesigner
        
        self.setWindowTitle("Ejemplo")  # Título de la ventana

        # Conectar botón a la función
        self.pushButton.clicked.connect(self.auto)
        self.current_value=0

    def funcion(self):
        if self.progressBar.value() < self.progressBar.maximum():
            self.progressBar.setValue(self.progressBar.value() + 5)
        else:
            self.progressBar.setValue(0)
            self.label.setText("BARRA COMPLETADA")
    
    def auto (self):
        for i in range (20):
            time.sleep(1)
            self.current_value += 5
            self.progressBar.setValue(self.current_value)

    
app = QtWidgets.QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
sys.exit(app.exec())
