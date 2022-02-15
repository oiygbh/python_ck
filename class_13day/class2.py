# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/2/15 10:41
from greenlet import greenlet
import time

"""
协程
"""


def work1():
    for i in range(10):
        print("=======work1======={}".format(i))
        g2.switch()
        time.sleep(0.1)


def work2():
    for i in range(10):
        print("=======work2======={}".format(i))
        g1.switch()
        time.sleep(0.1)


g1 = greenlet(work1)
g2 = greenlet(work2)
# 切换到g1中运行
g1.switch()