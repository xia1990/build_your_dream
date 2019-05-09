#!/usr/bin/python
#_*_ coding:utf-8 _*_
#遍历一个目录树，查找特定扩展的文件（.pdf和.jpg）,然后将它们拷贝到一个新文件夹中


import os
import shutil

filepath="/home/gerrit/python_script"
newpath="/home/gerrit/Test"

for root,dirs,files in os.walk(filepath):
    shutil.copytree(filepath,newpath,ignore=shutil.ignore_patterns("*.jpg","*.pdf"))
