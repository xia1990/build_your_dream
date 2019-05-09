#!/usr/bin/python
#_*_ coding:utf-8 _*_

import json
import xlwt
from collections import OrderedDict

with open("student.txt") as f:
    #json.loads将json数据转换成python对象
    #将读取的文件内容存放入字典
    d=json.loads(f.read())

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("student")

for row,i in enumerate(list(d)):
    worksheet.write(row,0,i)
    for col,j in enumerate(d[i]):
        worksheet.write(row,col+1,j)

    workbook.save("student.xls")
