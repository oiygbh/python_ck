# @Time : 2022/1/8 16:30 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
#  死锁案例
import threading
import time

a = 0


def func1():
    global a
    for i in range(1000000):
        mateA.acquire()  # 上锁
        mateB.acquire()  # 上锁
        print("----------")
        a += 1
        mateB.release()  # 上锁
        mateA.release()  # 释放锁
    print("线程1修改完a的值:", a)


def func2():
    global a
    for i in range(1000000):
        mateB.acquire()  # 上锁
        mateA.acquire()  # 上锁
        print("----------")
        a += 1
        mateA.release()  # 释放锁
        mateB.release()  # 释放锁
    print("线程2修改完a的值:", a)


#  创建锁
mateA = threading.Lock()
mateB = threading.Lock()
s_time = time.time()
t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()  # 开始执行线程1
t2.start()  # 开始执行线程2
e_time = time.time()
print("运行时间{}".format(e_time-s_time))
t1.join()
t2.join()



#  全局解释器锁GIL:控制线程运行