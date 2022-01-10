# @Time : 2022/1/7 21:39 
# @Author :jiale
# @File : class1.py 
# @Software: PyCharm
# 同步
# 异步
# 多线程
import threading
import time


def func1():
    for i in range(5):
        print("-----正在做事情1-----{}".format(threading.current_thread()))  # 返回正在运行的线程
        time.sleep(1)


def func2():
    for i in range(6):
        print("-----正在做事情2-----{}".format(threading.current_thread()))
        time.sleep(1)


# s_time = time.time()
# func1()
# func2()
# e_time = time.time()
# print("耗时：",e_time - s_time)
def main():
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    s_time = time.time()

    t1.setName('线程1')  # 设置线程名
    t2.setName('线程2')
    print(t1.is_alive())  # 线程是否执行
    t1.start()  # 开始执行线程1
    t2.start()  # 开始执行线程2
    print(t1.is_alive())  # 线程是否执行
    # 让主线程等待子线程执行完再继续往下执行
    print(threading.enumerate())  # 当前运行的所有线程对象
    print(threading.active_count())  # 返回当前执行线程的数量
    t1.join()  # 等待主线程运行时间，默认为线程运行结束
    t2.join()
    print(t1.getName())
    e_time = time.time()
    print(t2.getName())
    print("耗时：", e_time - s_time)


if __name__ == '__main__':
    main()
