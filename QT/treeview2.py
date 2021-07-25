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
        
        # QFileSystemModel.setRootPath(path) --> Root폴더 지정
        # QtCore.QDir.rootPath() --> Windows설치되어있는 루트 반환 (보통 C:\\)
        # 여기서 지정하는건 Model 객체의 Data 셋팅이고
        # View에서 보여줄 트리는 다시 셋팅 해줘야 함
        self.model = QFileSystemModel()
        self.model.setRootPath(r'\\10.21.10.204\fab 기술\fab기술\00_BackPart\06_심영현\설비별 알람 리스트\log_file')
        print(self.model.rootPath())

        # 1. Model.index 값 설정 (Root 위체)
        # 2. view.setRootIndex(1.Model.index 매개변수) 값 설정
        self.treeView.setModel(self.model)
        self.index_root = self.model.index(self.model.rootPath())
        self.treeView.setRootIndex(self.index_root)

        self.show()


app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())