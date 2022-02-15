# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/2/15 10:40
"""
生成器：
<1>生成器表达式
<2>在函数中使用yield这个关键字，这个函数就是生成器函数
"""
import time


def work1():
    for i in range(10):
        print("=======work1======={}".format(i))
        time.sleep(0.1)
        yield


def work2():
    for i in range(10):
        print("=======work2======={}".format(i))
        time.sleep(0.1)
        yield


# 通过生成器实现多任务
g1 = work1()  # 创建生成器
g2 = work2()

while True:
    try:

        next(g1)
        next(g2)
    except StopIteration:
        break
# 协程:微线程
"""
协程的本质是单任务，依赖于线程
协程相对线程来讲占用的资源更少(几乎不需要占什么资源)
yield这种机制称为协程
"""