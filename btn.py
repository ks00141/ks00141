from PyQt5.QtWidgets import QApplication, QPushButton, QRadioButton

class Btn(QPushButton,QRadioButton):
    def __init__(self,text,obj,x,y,width,height,type):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if type == "push":
            QPushButton.__init__(self.text,self.obj)
            self.setGeometry(self.x,self.y,self.width,self.height)

        elif type == "ridio":
            QRadioButton.__init__(self.text,self.obj)
            self.setGeometry(self.x,self.y,self.width,self.height)
        