
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QRadioButton, QButtonGroup
from PyQt5.QtCore import QCoreApplication
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    

    def set_driver(self,driver_path):
        return webdriver.Chrome(driver_path)
    

    def init_ui(self):
        
        self.setWindowTitle("test")
        self.setGeometry(1000,450,300,130)

        self.rbtn1 = QRadioButton("All",self)
        self.rbtn1.move(20,20)
        self.rbtn1.clicked.connect(self.each_clickcheck)

        self.rbtn2 = QRadioButton("TC",self)
        self.rbtn2.move(20,40)
        self.rbtn2.setAutoExclusive(False)
        self.rbtn2.clicked.connect(self.all_clickcheck)

        self.rbtn3 = QRadioButton("NS",self)
        self.rbtn3.move(20,60)
        self.rbtn3.setAutoExclusive(False)
        self.rbtn3.clicked.connect(self.all_clickcheck)

        self.rbtn4 = QRadioButton("PST",self)
        self.rbtn4.move(20,80)
        self.rbtn4.setAutoExclusive(False)
        self.rbtn4.clicked.connect(self.all_clickcheck)

        self.btn1 = QPushButton("스크랩",self)
        self.btn1.resize(100,20)
        self.btn1.move(100,25)
        self.btn1.clicked.connect(self.scrap)

        self.btn2 = QPushButton("open GW",self)
        self.btn2.resize(100,20)
        self.btn2.move(100,45)
        self.btn2.clicked.connect(self.openWeb)

        self.show()
    
    def all_clickcheck(self):
        if self.rbtn1.isChecked():
            self.rbtn1.setChecked(False)

    def each_clickcheck(self):
        self.each_check(self.rbtn2)
        self.each_check(self.rbtn3)
        self.each_check(self.rbtn4)
    
    def each_check(self,btn):
        if btn.isChecked():
            btn.setChecked(False)


    def scrap(self):
        check_list = []
        check_list.append((lambda btn : btn.text() if btn.isChecked() else None)(self.rbtn1))
        check_list.append((lambda btn : btn.text() if btn.isChecked() else None)(self.rbtn2))
        check_list.append((lambda btn : btn.text() if btn.isChecked() else None)(self.rbtn3))
        check_list.append((lambda btn : btn.text() if btn.isChecked() else None)(self.rbtn4))
        


    def openWeb(self):
        driver = self.set_driver("./chromedriver.exe")
        driver.get('http://gw.wisol.co.kr')
        id = driver.find_element_by_id('id')
        pwd = driver.find_element_by_id('password')
        id.send_keys("yhsim")
        pwd.send_keys("wisol1")
        pwd.send_keys(Keys.RETURN)
        
        self.popup_close(driver)
        self.goto_mail(driver)

    def popup_close(self,driver):
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

    def goto_mail(self,driver):
        driver.switch_to_frame('portalBody')
        driver.find_element_by_css_selector('#wrapMainFix > div.lnbContainer > div > div.nav > ul > li:nth-child(1) > a').click()
        driver.switch_to_frame('subBody')
        driver.switch_to_frame('menuFrame')
        driver.find_element_by_css_selector('#ext-gen10 > div > li:nth-child(4) > ul > li > div > a').click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = App()
    sys.exit(app.exec_())