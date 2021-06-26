import sys
from PyQt5.QtWidgets import QDialog, QApplication

class Set_up_user(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("test")
        self.show()

    def showModal(self):
        return super().exec_()