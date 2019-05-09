#!/usr/bin/python
#_*_ coding:utf-8 _*_
#给XML添加path属性值

import xml.etree.ElementTree as ET


def add_path():
    tree = ET.parse("manifest.xml")
    root=tree.getroot()

    for project in root.findall("project"):
        project_name=project.attrib['name']
        if 'path' in project.attrib.keys():
            pass    
        else:
            path_name=project_name
            project.set('path',path_name)

    ET.dump(root)
    tree.write("manifest.xml")

if __name__=="__main__":
    add_path()
