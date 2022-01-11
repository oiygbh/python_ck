# @Time : 2022/1/11 22:15 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
# 多进程之间通讯问题
from multiprocessing import Process, Queue
# from queue import Queue
import requests

# 创建队列添加10个任务


a = 1


def work1(q):

    while q.qsize() > 0:
        global a
        # 判断队列中是否有任务
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print("work1正在执行任务--{}".format(a))
        a += 1


def work2(q):
    while q.qsize() > 0:
        global a
        # 判断队列中是否有任务
        # 获取任务
        url = q.get()
        # 执行任务
        requests.get(url)
        print("work2正在执行任务--{}".format(a))
        a += 1


if __name__ == '__main__':
    # 创建进程
    q = Queue()
    for i in range(10):
        q.put("http://www.baidu.com")
    p1 = Process(target=work1,args=(q,))
    p2 = Process(target=work2,args=(q,))
    p1.start()
    p2.start()
