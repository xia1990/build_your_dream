#!/usr/bin/python
import sys
import json

sys.setrecursionlimit(1500)
dd={}
topList=[]

#读取data.json文件
with open('data.json') as jf:
	for line in jf.readlines():
		dd=json.loads(line)
		print dd
		

def getValue(key,topList):
	if key not in topList:
		topList.append(key)
		result=dd.get(str(key),"error")
		if result == "error":
			print "error"
			pass
		else:
			if len(result) == 0:
				return
			else:
				for subkey in result:
					getValue(subkey,topList)
			return topList

for key in dd.keys():
	getValue(key,topList)
	print topList
	
