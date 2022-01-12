# @Time : 2022/1/12 22:02 
# @Author :jiale
# @File : class4.py 
# @Software: PyCharm
# 进程池中的进程通信
from multiprocessing import Manager, Pool
import os, time


def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue中获取到信息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(5):
        q.put(i)


if __name__ == '__main__':
    print("(%s) start " % os.getpid())
    q = Manager().Queue()  # 使用Manager中的Queue
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(1)  # 先让上面的任务Queue存入数据，然后再让下面的任务开始从中取数据
    po.apply_async(reader, (q,))
    po.close()
    po.join()
