#!/usr/bin/python
#_*_ coding:utf-8 _*_

import xlrd
from xml.etree import ElementTree as ET

root=ET.Element("student")
son=ET.SubElement(student,'name')
son=ET.SubElement(student,'一个坑')
#son=ET.SubElement(root,'二个坑')

#son=ET.SubElement(root,'语文')
#son=ET.SubElement(root,'数学')

tree=ET.ElementTree(root)
tree.write('student.xml')
