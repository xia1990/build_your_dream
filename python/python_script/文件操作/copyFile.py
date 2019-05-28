#!/usr/bin/python
#_*_ coding:utf-8 _*_
#将.java和.txt考贝到指定文件中


import os
import shutil

test_dir=os.getcwd()
target_dir="/home/ubuntu/Test"
for root,dirs,files in os.walk(test_dir):
    for fname in files:
        if fname.endswith(".java") or fname.endswith(".txt"):
            print("copy...",fname)
            shutil.copy(fname,target_dir)
