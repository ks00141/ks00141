import os
import xml.etree.ElementTree as etree
import openpyxl
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.Qt import QFileSystemModel
from PyQt5 import QtCore

main_form,main_form_widget = uic.loadUiType("UI.ui")


class xmlFile():
    def __init__(self):
        self.ROOTPATH = "//10.21.10.204/fab 기술/fab기술/00_BackPart/06_심영현/설비별 알람 리스트/log_file"
        self.PATH = None
        self.WEEK = None
        self.TOOL = None
        self.fileList = None
        
    def setPATH(self):
        if(self.TOOL != None and self.WEEK != None):
            self.PATH = f"{self.ROOTPATH}/{self.WEEK}/#{self.TOOL}"
    
    def setWEEK(self):
        self.WEEK = input("WEEK ? ")
    
    def setTOOL(self):
        self.TOOL = input("TOOL ? ")
    
    def getPATH(self):
        return self.PATH
    
    def getWEEK(self):
        return self.WEEK

    def getTOOL(self):
        return self.TOOL

class xlsx():
    def __init__(self):   
        workBook = openpyxl.workBook()
        workBook.create_sheet("#9",0)
        workBook.create_sheet("#10",1)
        workBook.create_sheet("#11",2)
        workBook.create_sheet("#12",3)
    

class Main(main_form,main_form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        xml = xmlFile()

        self.model = QFileSystemModel()
        self.model.setRootPath(xml.ROOTPATH)
        self.treeView.setModel(self.model)
        self.index_root = self.model.index(self.model.rootPath())
        self.treeView.setRootIndex(self.index_root)
        self.setBtn.clicked.connect(self.set)
        self.createBtn.clicked.connect(self.created)

    def set(self):
        for file in os.listdir(self.model.filePath(self.treeView.currentIndex())):
            self.test = etree.parse(f"{self.model.filePath(self.treeView.currentIndex())}/{file}")
            self.desc = self.test.find("/Description")
            self.time = self.test.find("/TimeStamp")
            print(f"{self.time.text} / {self.desc.text}")

    def created(self):
        print(self.treeView.currentIndex().data())


app = QApplication(sys.argv)
w = Main()
sys.exit(app.exec_())