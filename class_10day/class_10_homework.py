# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/12 10:09
"""
1、什么是并发，什么是并行
并发（Concurrent）在操作系统中，是指一个时间段中有几个程序都处于已启动运行到运行完毕之间，且这几个程序都是在同一个处理机上运行。
就想前面提到的操作系统的时间片分时调度。打游戏和听音乐两件事情在同一个时间段内都是在同一台电脑上完成了从开始到结束的动作。
那么，就可以说听音乐和打游戏是并发的。

并行（Parallel），当系统有一个以上CPU时，当一个CPU执行一个进程时，另一个CPU可以执行另一个进程，
两个进程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)。
这里面有一个很重要的点，那就是系统要有多个CPU才会出现并行。在有多个CPU的情况下，才会出现真正意义上的『同时进行』。
"""


#  2、创建一个线程类，每个线程对http://httpbin.org/post发送100个请求，开启10个线程，同时发送，计算总耗时，分析平均耗时
import threading
import time

import requests


class ThreadRequests(threading.Thread):
    """
    发送request请求
    """

    def run(self):
        for i in range(100):
            res = requests.get('http://httpbin.org/post')
            print("Thread--{}--第{}次请求".format(self.name, i + 1))


# 创建五个线程，发起请求
def main():
    s_time = time.time()
    #  创建10个线程对象
    th = [ThreadRequests() for j in range(10)]
    #  遍历线程对象
    for i in th:
        i.start()
    #  遍历线程对象，让主线程等待子线程结束之后再往下执行
    for j in th:
        j.join()
    e_time = time.time()
    print("平均时间{}".format((e_time - s_time) / 1000))


main()