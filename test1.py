import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def console_out(self):
        print("test")

    def init_ui(self):
        self.setGeometry(100,100,600,600)
        btn = QPushButton("Push",self)
        btn.move(10,10)
        btn.clicked.connect(self.console_out)
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    sys.exit(app.exec_())