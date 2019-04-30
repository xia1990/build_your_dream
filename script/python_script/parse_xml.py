#!/usr/bin/python
#_*_ coding:utf-8 _*_
#如果当前行是project,就打印它的name值,和分支名称


import xml.etree.ElementTree as ET

tree=ET.parse("manifest.xml")
root=tree.getroot()
#print(root.tag)

for child in root.findall("default"):
    #得到默认分支
    default_revision=child.attrib['revision']

#遍历所有project的行
for project in root.iter("project"):
    #project.attrib输出的内容是一个dict
    #得到字典中所有的键
    #如果这个键中有revision这个属性，就使用默认值，如果没有就使用default行的属性
    if 'revision' in project.attrib.keys():
        project.attrib['revision']=project.attrib['revision']
    else:
        project.attrib['revision']=default_revision
		project.set('revision',default_revision)
    print(project.attrib['name'],project.attrib['revision'])
	
ET.dump(root)
tree.write("manifest.xml")


