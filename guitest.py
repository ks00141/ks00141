import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver

form = uic.loadUiType("./test1.ui")[0]



class App(QMainWindow,form):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.btn_open.clicked.connect(self.openweb)
        
        self.userset.triggered.connect(lambda: Set_window())
        
        self.show()

    def openweb(self):
        driver = webdriver.Chrome("./chromedriver.exe")
        driver.get("http://gw.wisol.co.kr")

app = QApplication(sys.argv)
w = App()
sys.exit(app.exec_())
