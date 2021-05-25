import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def test(self):
        print("Hi")
    

    def init_ui(self):
        self.setWindowTitle("test")
        self.setGeometry(100,100,50,200)
        btn = QPushButton("Push",self)
        btn.resize(btn.sizeHint())
        btn.move(50,100)
        btn.setToolTip("눌러보셈")
        btn.clicked.connect(self.test)
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    sys.exit(app.exec_())