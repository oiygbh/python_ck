# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/21 16:11
"""
1、多个装饰器装饰同一个函数
2、python中内置的三个装饰器
"""
import time

print("--------------------多个装饰器装饰同一个函数--------------------")


def wrapper(func):  # 计算函数运行时间
    print("函数运行时间装饰器")

    def count_time(*args, **kwargs):
        start_time = time.time()
        print("开始时间", start_time)
        func(*args, **kwargs)
        time.sleep(1)
        end_tine = time.time()
        print("结束时间", end_tine)
        print("函数运行的时间为:{:.5f}s".format(end_tine - start_time))

    return count_time  # 这里的'()'会导致报错'NoneType' object is not callable
    # 只要去掉count_time后面的括号即可解决问题


with open('user.txt') as f:
    users = eval(f.read())
print(users)


# print(users['user'])
# print(users['pwd'])
# print(users['token'])


def login_check(func_01):
    """
    登录验证装饰器
    :param func_01: type；functions
    :return:
    """

    def ado(*args, **kwargs):
        print("登录装饰器")
        if users["token"] is False:  # 判断token是否为false
            print("----------登录页面----------")
            username = input("输入账号：")
            password = input("输入密码：")
            # 登录校验
            if users["user"] == username and users["pwd"] == password:
                users["token"] = True  # 修改token值
                func_01(*args, **kwargs)  # 调用装饰器函数
        else:
            func_01()  # token值为True直接调用函数

    return ado


@login_check
def index():
    print("这里是网站首页")


@login_check  # count_time-->func=login_check(func)  func ==>ado
@wrapper  # func=wrapper(func)   func=count_time,从下往上装饰，从上往下执行
def func_02():
    time.sleep(2)
    print("这里是被装饰器装饰的函数")


# func_02()
print("--------------------多个装饰器装饰同一个函数--------------------")
print("--------------------类装饰器--------------------")


# 类装饰器
class MyTest(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def add(cls):  # 被@classmethod装饰之后，该方法就是一个类方法
        print('这个是类方法')
        print(cls)  # cls代表的是类本身

    @staticmethod
    def static():  # 默认没有参数,实例和类都可以调用
        print("这个是静态方法")

    @property  # 设定只读属性，只能读取不能修改
    def read_attr(self):
        print("这个装饰器装饰完了后该方法可以像属性一样被调用")
        return '@property修饰的类的属性，不能被修改'

    def sub(self):  # self代表的是实例本身
        print("sub中的self", self)


if __name__ == '__main__':
    # func_02()

    test = MyTest('toby')  # 初始化类
    test.name = 'lucky'  # 修改类属性name值
    print("修改后name的值：", test.name)
    test.sub()  # 调用类实例方法
    MyTest.add()  # 类方法可以直接被类调用
    # MyTest.sub()  #实例方法不能直接被类调用
    MyTest.static()   # 静态方法可以直接用类调用
    test.static()  # 静态方法也可以实例化调用
    test.read_attr  # @property修饰的方法，只能读取不能修改
    # test.read_attr = '19'  # 被property装饰的方法不可修改
    print(test.read_attr)
print("--------------------类装饰器--------------------")
