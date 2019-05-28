#!/usr/bin/python
#_*_ coding:utf-8 _*_
#除.txt和.py结尾的文件压缩

import zipfile
import os


test_dir=os.getcwd()
filename="wind.zip"
z=zipfile.ZipFile(filename,'w')
for root,dirs,files in os.walk(test_dir):
    for fname in files:
        if fname.endswith(".txt") or fname.endswith(".py"):
            continue
        print("Adding...",fname)
        z.write(os.getcwd(),fname)
z.close()


