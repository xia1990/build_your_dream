#!/usr/bin/python
#_*_ coding:utf-8 _*_

import json
import xlwt


with open("number.txt") as f:
    data=json.loads(f.read())
    print(type(data))

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("student")

i=0
for con in data:
    j=0
    for item in con:
        worksheet.write(i,j,item)
        j+=1
    i+=1
workbook.save("num.xls")
