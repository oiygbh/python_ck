# @Time : 2022/1/13 21:30 
# @Author :jiale
# @File : class_12_homework.py 
# @Software: PyCharm
"""
比较1000个任务队列
分别使用3个进程或线程完成，哪个更快？
# 进程快
任务数量少于CPU数量，并行
线程：全局解释器GIL的存在，并发(不可能同时执行三个任务)
"""
import requests, time
import queue  # 线程
from multiprocessing import Queue, Manager, Pool  # 进程
import threading

# 线程的队列，只能在一个进程中使用
q1 = queue.Queue()
for i in range(1000):
    q1.put("http://www.baidu.com")

# 进程的队列，可以在多个进程间通讯
# q2 = Queue()

# 进程池中的队列，给进程池中的各个进程之间使用
# q3 = Manager().Queue()
# for i in range(1000):
#     q3.put("http://www.baidu.com")

i = 0


# 线程函数
def work1():
    while q1.qsize() > 0:
        url = q1.get()
        requests.get(url=url)


# 进程函数
def work2(q3):
    while q3.qsize() > 0:
        url = q3.get()
        requests.get(url=url)
        global i
        i += 1
    print("------该进程运行了:%s次" % i)


def main():
    s_time = time.time()
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work1)
    t3 = threading.Thread(target=work1)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    e_time = time.time()
    print("线程耗时:{}".format(e_time - s_time))


if __name__ == '__main__':
    # main()  # 线程
    print("---------------进程-------------")
    q3 = Manager().Queue()
    for i in range(1000):
        q3.put("http://www.baidu.com")
    pool = Pool(3)
    s_time = time.time()
    for i in range(3):
        pool.apply_async(work2, args=(q3,))
    pool.close()
    pool.join()
    e_time = time.time()
    print("耗时:{:.2f}".format(e_time - s_time))
    # 进程耗时12.22
    print("---------------进程-------------")
