# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/2/15 10:41
import time
import requests
import gevent
from gevent import monkey
import queue
# 打补丁作用，只要有耗时的地方，自动切换任务，不局限于gevent.sleep()
monkey.patch_all()
"""
协程：gevent
协程存在与线程之中，线程默认不会等待协程执行
spawn；开启协程（第一个参数为协程要执行的任务）
join：让线程等待协程执行
协程之间切换的条件
gevent.sleep():协程耗时等待的情况下才会切换
gevent程序补丁：gevent.monkey.patch_all()
# 高并发首先考虑协程>线程>进程
"""
q=queue.Queue()
for i in range(1000):
    q.put("http://www.baidu.com")
# def work1():
#     for i in range(10):
#         print("=======work1======={}".format(i))
#         # gevent.sleep(0.1)
#         time.sleep(0.1)
#         requests.get("http://www.baidu.com")
#
#
# def work2():
#     for i in range(10):
#         print("=======work2======={}".format(i))
#         # gevent.sleep(0.1)
#         time.sleep(0.1)
#         requests.get("http://www.baidu.com")
def work():
    while q.qsize() > 0:
        url=q.get()
        requests.get(url)

# 创建两个协程
# g1 = gevent.spawn(work1)
# g2 = gevent.spawn(work2)
# 协程执行耗时
st=time.time()
g1 = gevent.spawn(work)
g2 = gevent.spawn(work)
g3 = gevent.spawn(work)  # 开的协程越多，耗时越短
g4 = gevent.spawn(work)
g5 = gevent.spawn(work)
g6 = gevent.spawn(work)
g1.join()
g2.join()
et=time.time()
print("耗时：{}".format(et-st))
