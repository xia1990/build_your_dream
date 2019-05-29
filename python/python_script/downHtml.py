#!/usr/bin/python
#_*_ coding:utf-8 _*_
#下载网页

import requests

r=requests.get("https://github.com/xia1990/wind-mobi/tree/master/python")
with open("a.html","wb") as f:
    f.write(r.content)
f.close()
