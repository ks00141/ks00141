from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton

class Btn(QPushButton):
    def __init__(self,text,obj,x,y,width,height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        super().__init__(self.text,obj)
        self.setGeometry(self.x,self.y,self.width,self.height)
        