import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form = uic.loadUiType("test.ui")[0]

class App(QMainWindow,form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda :print("Hi"))

app = QApplication(sys.argv)

w = App()
w.show()

app.exec_()