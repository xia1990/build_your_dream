#!/usr/bin/python
#_*_ coding:utf-8 _*_
#打映大于100MB的文件

import os

test_dir=os.getcwd()
for root,dirs,files in os.walk(test_dir):
    for filename in files:
        if os.path.getsize(filename)>100:
            print(os.path.join(root,filename))
