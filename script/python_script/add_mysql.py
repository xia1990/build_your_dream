#!/usr/bin/python
#_*_ coding:utf-8 _*_
#添加数据


import pymysql

conn=pymysql.connect(host="192.168.56.101",user="root",passwd="root",database="cesudb")
cursor=conn.cursor()
#向数据库表中添加数据
sql="insert into user1(name,age) value (%s,%s);"
#单个执行
#username="Alex"
#age=18

#批量添加
data=[("kate",22),("rose",19),("lily",20)]

try:
    #执行单条语句
    #cursor.execute(sql,[username,age])
    #执行插入多条SQL语句
    cursor.executemany(sql,data)
    #提交事物
    conn.commit()
    #得到数据ID
    last_id=cursor.lastrowid
except Exception as e:
    #有异常,回滚事务
    conn.rollback()

cursor.close()
conn.close()

