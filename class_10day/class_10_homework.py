# @Time : 2022/1/8 15:19 
# @Author :jiale
# @File : class_10_homework.py 
# @Software: PyCharm
#  1、什么是并发，什么是并行


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