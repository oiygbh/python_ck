# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/12 11:13
# 多进程
# 多进程执行多任务
from multiprocessing import Process
import time

# 多进程不共享全局变量
a = 0


def work1():
    global a
    for i in range(10):
        print("---任务1---{}".format(a))
        a += 1
        time.sleep(0.5)


def work2():
    global a
    for i in range(10):
        print("---任务2---{}".format(a))
        a += 1
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程
    p1 = Process(target=work1())
    p2 = Process(target=work2())
    p1.start()
    p2.start()
# 进程执行时不加__name__=='__main__'会报错
# 无限递归
