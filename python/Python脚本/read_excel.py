#!/usr/bin/python3
#_*_ coding:utf-8 _*_
#读取excel表格内容输出成json格式

import xlrd
import json

#打开一个excel表格
data=xlrd.open_workbook("abc.xls")
table=data.sheets()[0]
#得到表格的行和列
ncols=table.ncols
nrows=table.nrows
d1={}

def read_excel():
    for i in range(1,ncols):
		#第3行和第4行的类容
        row1_content=table.cell_value(2,i).encode("utf-8")
        row2_content=table.cell_value(3,i).encode("utf-8")

		#把内容存放到字典中
        d1[row1_content]=row2_content
		#把字典转换成json格式输出
        d2=json.dumps(d1,encoding="utf-8",ensure_ascii=False,indent=4)
        print(d2)


if __name__=="__main__":
    read_excel()
