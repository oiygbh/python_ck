# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/29 15:57
# 一、实现一个操作mysql的上下文管理器，可以自动断开连接
import pymysql as pymysql


class DB:
    # 数据库操作上下文管理器
    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)  # 连接数据库
        self.cursor = self.con.cursor()  # 获取游标

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


DATABASE_CONF = dict(
    host='localhost',
    user='test',
    password='test',
    database='test',
    port=3306,
    charset='utf8')
with DB(DATABASE_CONF) as cur:
    cur.execute('select * from bw_user WHERE uid = 1032')
    print(cur.fetchone())

"""
二、描述__slots__属性的作用，并修改读取excel类中保存测试用例的类
1、限制对象属性，指定指定的slots的属性
2、节约内存
3、不可被继承
"""


class Case:
    __slots__ = ['case_id', 'title', 'url', 'data', 'excepted']

    def __init__(self):
        self.case_id = None
        self.title = None
        self.url = None
        self.data = None
        self.excepted = None


"""
3、面向对象的三大特征是什么，多态又是什么
特征：封装、继承、多态
多态：指的是一类事物有多种形态，一个抽象类有多个字类，不同的字类对象调用相同的方法，产生不同的执行结果
4、私有属性怎么定义，不同的定义方式有什么区别
单下划线、双下划线开头
单下划线开头的，对外是公开的，可以直接访问
双下划线开头的，对外不能直接访问，为了保护这个变量，在原有的属性名前加了一个 _类名
"""
