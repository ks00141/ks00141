import sys
from selenium import webdriver
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton
from btn import Btn


class App(QMainWindow):

    btn_width,btn_height = 50,50

    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setGeometry(100,100,300,300)
        btn1 = Btn("조회",self,10,100,self.btn_width,self.btn_height)
        

        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    sys.exit(app.exec_())