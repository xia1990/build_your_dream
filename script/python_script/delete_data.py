#!/usr/bin/python
#_*_ coding:utf-8 _*_

import pymysql

conn=pymysql.connect(host="192.168.56.101",user="root",passwd="root",db="cesudb")
cursor=conn.cursor()
sql="delete from user1 where id=%s"
try:
    cursor.execute(sql,[9])
    #提交事务
    conn.commit()
except Exception as e:
    #有异常,回滚事务
    conn.rollback()

#关闭所有连接
cursor.close()
conn.close()

