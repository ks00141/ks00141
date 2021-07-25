import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from PyQt5 import uic
# 파일탐색기 구조로 Model 구성하려면 QFIleSystemModel 써야함
from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore

main_form = uic.loadUiType('main.ui')[0]

class Main(QMainWindow,main_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # QFileSystemModel --> Root 폴더를 지정해주면 알아서 불러와주는듯
        # QFileSystemModel.setRootPath(path) --> Root폴더 지정
        # QtCore.QDir.rootPath() --> Windows설치되어있는 루트 반환 (보통 C:\\)
        self.model = QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.rootPath())


        self.treeView.setModel(self.model)

        self.show()


app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())