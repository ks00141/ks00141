from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

main_window = uic.loadUiType('main.ui')[0]


class Main(QMainWindow, main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())