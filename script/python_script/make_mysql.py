#!/usr/bin/python
#_*_ coding:utf-8 _*_

import pymysql

conn=pymysql.connect(host="192.168.56.101",user="root",passwd="root",db="cesudb")
cursor=conn.cursor()

def create_table():
    sql="""
    create table people(
    id int auto_increment primary key,
    name char(10) not null unique,
    age tinyint not null,
    sex char(10)
    )engine=innodb default charset=utf8;
    """
    cursor.execute(sql)

def add():
    sql="insert into people (name,age,sex) values (%s,%s,%s);"
    name="杨洋"
    age=18
    sex="男"
    try:
        cursor.execute(sql,[name,age,sex])
        conn.commit()
    except Exception as e:
        conn.rollback()


def add_2():
    sql="insert into people (name,age,sex) values (%s,%s,%s);"
    data=[("aaa",20,'F'),('bbb',20,'M'),('ccc',20,'M')]
    try:
        cursor.executemany(sql,data)
        conn.commit()
    except Exception as e:
        conn.rollback()


def update():
    sql="update people set age=%s where name=%s"
    username="aaa"
    age=100
    try:
        cursor.execute(sql,[age,username])
        conn.commit()
    except Exception as e:
        conn.rollback()

def delete():
    sql="delete from people where id=%s;"
    try:
        cursor.execute(sql,[1])
        conn.commit()
    except Exception as e:
        conn.rollback()

def select():
    sql="select id,name,age,sex from people where id=2"
    cursor.execute(sql)
    #查询单条语句
    ret=cursor.fetchone()
    print(ret)

def find():
    sql="select * from people;"
    cursor.execute(sql)
    ret=cursor.fetchall()
    print(ret)

if __name__=="__main__":
    #create_table()
    #add()
    #add_2()
    #update()
    #delete()
    #select()
    find()
    cursor.close()
    conn.close()
