import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# UI File Load / uic.loadUiType("FileName")
# UI->Python Class로 변환한 코드 / GUI QtWidget 반환해줌
main_form,main_form_widget = uic.loadUiType("test1.ui")
user_set_form,user_set_form_widget = uic.loadUiType("userset.ui")

# loadUiType으로부터 반환받은 Class 두개 다중상속하여 MainWindow 정의
# QtWidget Class로 기본틀 생성
# 변환된 UI Class로 재구성 (setupUi)

class Main(main_form,main_form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.ID = None
        self.PWD = None
        # click이 아닌 Action (Menu) 스위치를 On한다는 의미로 triggereg가 쓰인듯 함
        # Triggered Method 사용하여 Event Slot 등록
        self.userset.triggered.connect(self.open_dialog)
        self.btn_open.clicked.connect(self.open_web)

    
        # 창유지가 안됨 왜냐하면 Userset 창에 대한 이벤트루프가 안돌기 때문
        # 이렇게만 코드를 짜면 서로 다른 독립적인 두창이 이벤트에 의해 실행되는 것뿐
        # 1. Userset 창을 Main창에 종속시켜버리기(Main창 이벤트 루프가 계속 돌아서 유지되는듯)
        # Userset(self) <- self = parent instance이기 때문에 부모 객체가 두번째 인자로 들어감
        # Userset Class 초기화시 parent를 인자로 넘겨 종속시켜버리기
        # 이렇게 되면 Sub 창 생성은 되나 비동기로 실행 되는듯??
        # 2. 따로 Userset 창 이벤트 루프 만들기 (exec())
        # userset.exec_()

    def open_dialog(self):
        userset = Userset()
        userset.exec_()
        if userset.ID and userset.PWD:
            self.ID = userset.ID
            self.PWD = userset.PWD
            
        

    def open_web(self):
        if self.ID and self.PWD:
            driver = webdriver.Chrome("./chromedriver.exe")
            driver.get("http://gw.wisol.co.kr")
            id = driver.find_element_by_xpath('//*[@id="id"]')
            pwd = driver.find_element_by_xpath('//*[@id="password"]')
            id.send_keys(self.ID)
            pwd.send_keys(self.PWD)
            pwd.send_keys(Keys.RETURN)


# MainWindow와 동일하게 Dialog Calss 정의
class Userset(user_set_form_widget,user_set_form):

    # 메인창에서 메인창 객체가 안넘길수도 있기때문에 기본값 None으로 주는게 좋음
    def __init__(self,parent=None):

        # 틀만들때 메인창 같이 넘겨서 종속시켜 버리기
        super().__init__(parent)
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.set_info)
        self.ID,self.PWD = None,None
    
    #pushBtn 클릭시 Main창으로 ID/PWD 값 넘겨주기
    def set_info(self):
        self.ID = self.id_text.text()
        self.PWD = self.pwd_text.text()
        self.close()

app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())