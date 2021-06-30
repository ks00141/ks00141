import sys
from PyQt5.QtWidgets import *

class TestUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        # Action 객체 만들기 / 종속될 부모 객체가 두번재 인자로 들어가야함
        action1 = QAction('1번입니다.',self)
        # Event Slot 등록 (click X triggered를 사용 / 아마 작동시킨다는 개념이라 그런듯)
        # 트리거가 켜질때 = 스위치 On = 가동될때 이런 의미 인듯
        action1.triggered.connect(self.open_dialog)

        # Menubar 생성
        menubar = self.menuBar()
        # Menu 생성
        fileMenu = menubar.addMenu("test")
        # Menu - Action 객체 연결
        fileMenu.addAction(action1)

        self.show()

    def open_dialog(self):
        self.dialog = QDialog()
        self.dialog.show()

App = QApplication(sys.argv)
w = TestUi()
sys.exit(App.exec_())
