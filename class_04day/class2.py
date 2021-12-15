# @Time : 2021/12/15 21:36 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
print("----------带参数装饰器----------")
# def add(func):
#     def fun(a,b):
#         print('相乘',a*b)
#         print('相除',a/b)
#         print('相减',a-b)
#         func(a,b)
#     return fun
# @add
# def add_num(a,b):
#     # 打印两个数相加
#     print('相加',a+b)
# add_num(11,22)
print("-----------带参数装饰器----------")
print("-----------通用装饰器----------")
# 通用装饰器
def add(func):
    # *args  元组
    # **kwargs 字典
    def fun(*args, **kwargs):
        print(args)
        print(**kwargs)
        print("调用装饰器的功能代码：登录")
        return func(*args, **kwargs)   #  装饰类必须写return

    return fun

@add
def index():
    print("这是网站首页")

@add
def good_list(num):
    print("这是商品列表第{}页".format(num))
index()
good_list(9)
print("-----------通用装饰器----------")
print("-----------装饰器装饰类----------")
@add  # MyClass=add(MyClass)
class MyClass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass
m = MyClass("toby","26")
print(m)
# 1、用类实现装饰器
# 2、多个装饰器装饰同一个函数
# 3、python中类里面三个内置的装饰器