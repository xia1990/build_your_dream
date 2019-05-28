#!/usr/bin/python
#_*_ coding:utf-8 _*_
#批量修改文件名前缀

import os

folder_name=raw_input("请输入文件夹的名字：")

for name in os.listdir(folder_name):
    print(name)
    os.rename(name,'[wing]-'+name)
    
