import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QPushButton, QRadioButton

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("test")
        
        self.btn = Btn("test",self,"push")

        self.show()


class Btn(QPushButton,QRadioButton):
    def __init__(self,text,obj,type):
        if type == "push":
            QPushButton().__init__(text,obj)
        elif type == "radio":
            QRadioButton().__init__(text,obj)

app = QApplication(sys.argv)
w = App()
sys.exit(app.exec_())