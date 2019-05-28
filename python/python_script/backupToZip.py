#!/usr/bin/python
#_*_ coding:utf-8 _*_

import zipfile
import os


def backuptoZip(folder):
    folder=os.path.abspath(folder)
    number=1
    while True:
        #压缩的文件名称
        filename=os.path.abspath(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(filename):
            break
        number=number+1
    z=zipfile.ZipFile(filename,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        z.write(foldername)
        for filename in filenames:
            print("Adding files in %s..." % (foldername))
            #z.write(os.path.join(foldername,filename))
            z.write(os.getcwd(),filename)
    z.close()
    print('number',number)

backuptoZip(".")


