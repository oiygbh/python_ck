# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/2/15 10:39
"""
比较1000个任务队列
分别使用3个进程或线程完成，哪个更快？
# 进程快
任务数量少于CPU数量，并行
线程：全局解释器GIL的存在，并发(不可能同时执行三个任务)
"""
# 使用进程运行
import requests, time
from multiprocessing import Queue, Manager, Pool  # 进程
import threading

i = 0


def work(q3):
    while q3.qsize() > 0:
        url = q3.get()
        requests.get(url=url)
        global i
        i += 1
    print("------该进程运行了:%s次" % i)


if __name__ == '__main__':
    print("---------------进程运行-------------")
    q3 = Manager().Queue()
    for i in range(1000):
        q3.put("http://www.baidu.com")
    pool = Pool(3)
    s_time = time.time()
    for i in range(3):
        pool.apply_async(work, args=(q3,))
    pool.close()
    pool.join()
    e_time = time.time()
    print("耗时:{:.2f}".format(e_time - s_time))
    # 进程耗时12.22
    print("---------------进程运行-------------")