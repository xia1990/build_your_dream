#!/usr/bin/python
#_*_ coding:utf-8 _*_

import zipfile
import os

filename="FlashPackage_S102X_32_Factory_QFIL.zip"
testdir="./out"
z=zipfile.ZipFile(filename,"w")
if os.path.isdir(testdir):
    for d in os.listdir(testdir):
        print("Adding...",d)
        #z.write(testdir+os.sep+d)
        z.write(testdir+os.sep+d)
z.close()
