#!/usr/bin/python
#_*_ coding:utf-8 _*_


import re
import shutil
import os


dataPattern=re.compile(r'''^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$''',re.VERBOSE)
for amerFilename in os.listdir("."):
    print("os.getcwd()=%s" % os.getcwd())
    mo=dataPattern.search(amerFilename)
    if mo==None:
        continue
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)
    print('Renaming "%s" to "%s" ...' %(amerFilename,euroFilename))

