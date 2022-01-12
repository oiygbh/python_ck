# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/12 10:06
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


if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()  # 开始执行线程1
    t2.start()  # 开始执行线程2
