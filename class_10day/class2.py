# @Time : 2022/1/7 22:18 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
# 通过继承Tread类创建线程,重写run方法
import threading
import time

import requests


class RequestThread(threading.Thread):
    """
    发送request请求
    """
    def __init__(self,url):  # 传参需要重写__init__方法，重写后调用父类__init__方法
        self.url=url
        super().__init__()

    def run(self):
        for i in range(10):
            res = requests.get(self.url)
            print("线程{}--返回的状态码--{}".format(threading.current_thread(), res.status_code))


# 创建五个线程，发起请求
s_time = time.time()
for i in range(5):
    t = RequestThread("http://www.baidu.com")

    t.start()
e_time = time.time()
print("耗时：", e_time - s_time)
