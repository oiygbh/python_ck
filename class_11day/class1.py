# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/12 11:08
#  互斥锁
import threading
import time

a = 0


def func1():
    global a
    for i in range(10000):
        mate.acquire()  # 上锁
        a += 1
        mate.release()  # 释放锁
    print("线程1修改完a的值:", a)


def func2():
    global a
    for i in range(10000):
        mate.acquire()  # 上锁
        a += 1
        mate.release()  # 释放锁
    print("线程2修改完a的值:", a)


#  创建锁
mate = threading.Lock()
s_time = time.time()
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()  # 开始执行线程1
t2.start()  # 开始执行线程2
e_time = time.time()
print("运行时间{}".format(e_time-s_time))
t1.join()
t2.join()