# @Time : 2022/1/7 22:34 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
#  多线程全局变量问题
import threading
import time

a = 100


def func1():
    global a
    for i in range(1000):
        a += 1
    print("线程1修改完a的值:", a)


def func2():
    global a
    for i in range(1000):
        a += 1
    print("线程2修改完a的值:", a)


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t1.start()  # 开始执行线程1
t2.start()  # 开始执行线程2
