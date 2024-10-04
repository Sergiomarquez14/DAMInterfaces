import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("La calculadora")
        self.setGeometry(600, 300, 300, 300)

        self.resultado = QLineEdit()
        layout = QGridLayout()
        layout.addWidget(self.resultado, 0, 0, 1, 4)

        nombre_boton = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "*"],
            ["0", "/", ".", "=",],
            ["(",")","%","C"]
        ]
        for i in range(1, 6 ):
            for j in range(0, 4):
                boton = QPushButton(nombre_boton[i-1][j])
                boton.clicked.connect(self.press_button) 
                layout.addWidget(boton, i, j)

        self.setLayout(layout)

    def press_button(self):
        sender = self.sender()
        if(sender.text()=="="):
            self.resultado.setText(str(eval(self.resultado.text())))
        else:
            self.resultado.setText(self.resultado.text() + sender.text())
        if(sender.text()=="C"):
            self.resultado.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec())
