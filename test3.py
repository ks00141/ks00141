# 책임님 cvs 파일 변환

import os
import csv
import openpyxl
from openpyxl import workbook

tools = ["1호기","2호기"]



for tool in tools:
    dirPath = f'C:/Users/wisol/Desktop/Daily Check/{tool}/Daily Check'
    filelist = os.listdir(dirPath)
    workBook = openpyxl.Workbook()
    workSheet = workBook.active
    workSheet.append(["일자",1,2,3,4,5])
    for fileName in filelist:
        file = open(f"{dirPath}/{fileName}/{fileName}.csv","r")
        data = list(csv.reader(file))
        workSheet.append([fileName,(data[0][22]),(data[0][25]),(data[0][28]),(data[0][31]),(data[0][34])])
        file.close()

    workBook.save(f"C:/Users/wisol/Desktop/{tool}.xlsx")