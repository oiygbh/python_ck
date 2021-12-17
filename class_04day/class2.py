# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/17 11:35

print("--------------------带参数装饰器--------------------")


def extend_add(func_01):
    def fun(a, b):
        print('相乘:', a * b)
        print('相除:', a / b)
        print('相减:', a - b)
        func_01(a, b)

    return fun


@extend_add
def add_num(a, b):  # 在此功能上，再实现两个数的乘法、除法、减法，使用装饰器
    # 打印两个数相加
    print('相加:', a + b)


add_num(11, 22)  # 调用函数,等同与add(add_num(11,22))
print("--------------------带参数装饰器--------------------")
print("--------------------通用装饰器装饰类--------------------")


# 通用装饰器
def common(func):
    # *args  元组
    # **kwargs 字典
    def fun_01(*args, **kwargs):
        print("字典参数:",args)
        print("关键字参数:",**kwargs)
        print("调用装饰器的功能代码：登录")
        return func(*args, **kwargs)  # 装饰类必须写return，装饰函数可以不写

    return fun_01


@common
def index():
    print("这是网站首页")


@common
def goods_list(num):
    print("这是商品列表第{}页".format(num))


index()
goods_list(9)
print("--------------------通用装饰器装饰类--------------------")
print("--------------------装饰器装饰类--------------------")


@common  # MyClass=common(MyClass)
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


m = MyClass("toby", "26")
print(m)
# 1、用类实现装饰器
# 2、多个装饰器装饰同一个函数
# 3、python中类里面三个内置的装饰器
print("--------------------装饰器装饰类--------------------")