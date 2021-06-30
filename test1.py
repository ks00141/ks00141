import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form = uic.loadUiType("test1.ui")[0]
userform = uic.loadUiType("userset.ui")[0]

class App(QMainWindow,form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.userset.triggered.connect(self.open_dialog)
        self.show()

    def open_dialog(self):
        Userset(self)
        print(uic.loadUiType("userset.ui")[0].setupUi)

class Userset(QDialog,userform):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.show()
        


app = QApplication(sys.argv)
w = App()
sys.exit(app.exec_())

