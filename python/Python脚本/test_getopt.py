#!/usr/bin/python
#_*_ coding:utf-8 _*_

import getopt
import sys

def usage():
    print("-h --help display the help information")

options,args=getopt.getopt(sys.argv[1:],"ha:b:",["help","atest=","btest="])

for name,value in options:
    if name in ("-h","--help"):
        usage()
        sys.exit()
    elif name in ("-a","--atest"):
        print("atest is:",value)
    elif name in ("-b","--btest"):
        print("btest is:",value)
