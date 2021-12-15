# @Time : 2021/12/15 22:18 
# @Author :jiale
# @File : class_04_homework.py 
# @Software: PyCharm
"""
1、一个完整的闭包必须满足哪几个条件
2、定义一个计算函数运行时间的装饰器(计算时间使用time模块实现)
3、编写装饰器，为多个函数加上认证的功能(用户的账号密码来自文件)，要求登录成功一次，后续的函数都无须再输入账号和密码
"""
#2、
import time


def wrapper(func):
    def count_time(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_tine=time.time()
        print("函数运行的时间为:{:.5f}".format(start_time-end_tine))
        return count_time()