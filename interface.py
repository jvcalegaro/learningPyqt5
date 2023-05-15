#import bla
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Pimeira janela"
        
        botao1 = QPushButton("Botao 1", self)
        botao1.move(50, 50)
        botao1.resize(150, 50)
        botao1.setStyleSheet('QPushButton {background-color: #999999;font:bold;font-size:20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton("Botao 2", self)
        botao2.move(300, 50)
        botao2.resize(150, 50)
        botao2.setStyleSheet('QPushButton {background-color: #999999;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('1, 2, 3 indiozinhos!')

    def botao2_click(self):
        print('4, 5, 6 indiozinhos!')    


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())