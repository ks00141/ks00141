import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        sb = self.statusBar()
        sb.showMessage("Ready")
        mb = self.menuBar()
        mb.addMenu("1")

        btn1 = QPushButton("Hi",self)
        btn2 = QPushButton("Bye",self)

        btn1.move(20,250)
        btn2.move(220,250)

        btn1.clicked.connect(lambda:sb.showMessage("Hi"))
        btn2.clicked.connect(lambda:sb.showMessage("Bye"))
        self.setGeometry(100,100,500,500)
        self.show()



app = QApplication(sys.argv)
w = App()
sys.exit(app.exec_())