# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/29 16:16
# 经典类，继承：instance类型，python2
class MyClass(object):
    pass


# 新式类，继承：object,python3
class Test(object):
    pass


t = Test()
print(type(t))
print(type(Test))
print(type(type))
# type：python中所有的类都是通过type来创建出来的,type是元类
# object：python3中所有类的顶级父类
