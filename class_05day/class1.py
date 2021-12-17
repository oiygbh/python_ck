# @Time : 2021/12/17 21:33 
# @Author :jiale
# @File : class1.py 
# @Software: PyCharm
"""
1、多个装饰器装饰同一个函数
2、python中内置的三个装饰器
"""
import time


def wrapper(func):
    def count_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_tine = time.time()
        print("函数运行的时间为:{:.5f}".format(start_time - end_tine))

    return count_time()


with open('user.txt') as f:
    users = eval(f.read())
print(users)
print(users['user'])
print(users['pwd'])
print(users['token'])


def login_check(func):
    """
    登录验证装饰器
    :param func_01: type；functions
    :return:
    """

    def ado(*args, **kwargs):
        if users["token"] is False:  # 判断token是否为false
            print("----------登录页面----------")
            username = input("输入账号：")
            password = input("输入密码：")
            # 登录校验
            if users["user"] == username and users["pwd"] == password:
                users["token"] == True  # 修改token值
                func(*args, **kwargs)  # 调用装饰器函数
        else:
            func()  # token值为True直接调用函数

    return ado


@login_check
def index():
    print("这里是网站首页")


@login_check
def page1():
    print("这里是page1页面")


@login_check
def page2():
    print("这里是page2页面")


@login_check # count_time-->func=login_check(func)  func ==>ado
@wrapper  # func=wrapper(func)   func=count_time,从下往上装饰，从上往下执行
def func_01():
    time.sleep(2)
    print("这里是需要被装饰器装饰的函数")


func_01()
