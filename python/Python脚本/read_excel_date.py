#!/usr/bin/python
#_*_ coding:utf-8 _*_
#解析EXCEL表格中的日期


import xlrd
import datetime
import time

data=xlrd.open_workbook("new.xls")
table=data.sheet_by_index(0)

for row in range(0,table.nrows):
    date=xlrd.xldate_as_tuple(table.cell(row,0).value,0)
    #value=datetime.datetime(*date)
    day_one="%s/%s/%s" % (date[0],date[1],date[2])
    print(day_one)
