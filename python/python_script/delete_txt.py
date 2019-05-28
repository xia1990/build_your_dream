#!/usr/bin/python
#_*_ coding:utf-8 _*_
#删除指定后缀结尾的文件

import os

source_dir=os.getcwd()

for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        os.unlink(filename)
