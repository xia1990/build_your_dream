#!/usr/bin/python
#_*_ coding:utf-8 _*_
#生成验证码

import random

checkcode=''
for i in range(4):
    current=random.randrange(0,4)
    print current
    if current != i:
        temp=chr(random.randint(65,90))
    else:
        temp=random.randint(0,9)
    checkcode+=str(temp)

print checkcode
