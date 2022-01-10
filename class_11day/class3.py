# @Time : 2022/1/10 21:37 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
# IO cpu
import threading

import time

import requests

a = 0


def func1():
    global a
    for i in range(10000000):
        a += 2


def func2():
    global a
    for i in range(10000000):
        a += 2


def func3():
    for i in range(50):
        requests.get('http://httpbin.org/post')


def func4():
    for i in range(50):
        requests.get('http://httpbin.org/post')


s_time = time.time()
# t1 = threading.Thread(target=func3)
# t2 = threading.Thread(target=func4)
#
# t1.start()  # 开始执行线程1
# t2.start()  # 开始执行线程2
# t1.join()
# t2.join()
# ------------------cpu密集型-----------------------
# 单线程和多线程差别不大
# func1()
# func2()
# --------------------网络io密集型---------------------
# 多线程耗时远低于单线程
func3()
func4()
e_time = time.time()
print("运行时间{}".format(e_time - s_time))


