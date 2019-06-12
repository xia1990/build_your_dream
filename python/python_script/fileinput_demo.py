#!/usr/bin/python
#_*_ coding:utf-8 _*_


import fileinput
import glob


for line in fileinput.input(glob.glob("test*.txt")):
    if fileinput.isfirstline():
        print('-'*20,'Reading %s...' % fileinput.filename(),'-'*20)
    print(str(fileinput.lineno())+':'+line.upper())
