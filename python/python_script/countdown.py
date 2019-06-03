#!/usr/bin/python
#_*_ coding:utf-8 _*_
#倒计时

import time
import subprocess

timeLeft=60
while timeLeft>0:
    print(timeLeft)
    time.sleep(1)
    timeLeft=timeLeft - 1

