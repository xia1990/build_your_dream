#!/usr/bin/python
#_*_ coding:utf-8 _*_

import os
import re
import shutil

test_dir=os.getcwd()
#查找指定前缀的文件
list_file=[i for i in os.listdir(test_dir) if i.startswith("abc")]

#定位缺失的编号
numRegex = re.compile(r'^abc(.*?).txt$')
num_list1=[]
for i in list_file:
    match=numRegex.search(i)
    num_list1.append(match.group(1))
#print('num_list1:',num_list1)

#存储目标文件中的数字的数组
num_list2=[]
for j in range(1,len(num_list1)+1):
    t_i='%03d' % j
    num_list2.append(j)
#print('num_list2:',num_list2)

#如果在目标中存在，但不在原始中存在，则为缺失的编号文件
for m in num_list2:
    if m not in num_list1:
        print("abc%s.txt" % m)
#修改后面的文件名，让缺失的消失
for a,v in zip(num_list1,num_list2):
    shutil.move("abc%s.txt"%a,"abc%s.txt"%v)

print('Rename project is done!')
