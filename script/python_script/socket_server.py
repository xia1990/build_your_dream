#!/usr/bin/python
#_*_ encoding:utf-8 _*_

import socket

ip_port=("127.0.0.1",9999)

sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

while True:
    inp=raw_input("数据：").strip()
    if inp=='exit':
        break
    sk.sendto(inp,ip_port)

sk.close()

