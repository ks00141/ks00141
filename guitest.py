import sys
from selenium import webdriver
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def open_web(self):
        print("test")

    def init_ui(self):
        self.setGeometry(100,100,300,300)
        btn = QPushButton("click",self)
        btn.clicked.connect(self.open_web)
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    sys.exit(app.exec_())