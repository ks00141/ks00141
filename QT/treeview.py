import sys
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import Qt

# QTreeWidget 는 MVC패턴을 적용해야 한다
# 즉 Data를 다루는 Model, 화면에 표현을 담당하는 View 따로 만들어야함
# Model = QStandItemModel
# View = QTreeView

main_form = uic.loadUiType('main.ui')[0]

class Main(QMainWindow, main_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # QstandardItemModel(Row,Column)
        # QstandardItemMode.(column index,orientation,'text')
        model = QStandardItemModel(0,2)
        model.setHeaderData(0, Qt.Horizontal,'Time')
        model.setHeaderData(1, Qt.Horizontal,'Description')

        # insertRow(row) = 행 입력 인덱스
        # model.setData(model.index(row,column),Data)

        model.insertRow(0)
        model.setData(model.index(0,0),'00:00:00')
        model.setData(model.index(0,1),'test')
        print(model.index(0,0))

        # view(QTreeWidget)에 Model(QStandardModel) 바인딩하기
        self.treeView.setModel(model)
        self.show()
        

app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())