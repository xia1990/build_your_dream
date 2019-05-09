#!/usr/bin/python
#_*_ coding:utf-8 _*_

import xlwt
import json

with open("city.txt") as f:
    data=json.loads(f.read())
    print(type(data))

workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("city")

i=0
for k in data:
    worksheet.write(i,0,k)
    worksheet.write(i,1,data.get(k))
    i+=1
workbook.save("city.xls")

