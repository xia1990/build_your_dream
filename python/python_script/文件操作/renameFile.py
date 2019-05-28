#!/usr/bin/python
#_*_ coding:utf-8 _*_
#批量修改文件后缀

import os

test_dir=os.getcwd()
for root,dirs,files in os.walk(test_dir):
    for fname in files:
        if fname.endswith(".java"):
            #os.path.splitext：将文件分成名字+后缀的形式
            newname=os.path.splitext(fname)[0]+'.c'
            print("rename...",fname)
            os.rename(fname,newname)
