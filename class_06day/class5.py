# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/27 10:24
#  __slots__,限制对象的属性
class Base(object):
    # 限制类对象所能绑定的属性
    #  节约内存
    #  节约内存：定义了__slots__属性之后，那么该对象不会再自动生成__dict__属性
    __slots__ = ['name']

    # 初始化函数也只能有name属性
    def __init__(self, name):
        self.name = name

    pass


b = Base()
# b.age=19  #  报错，不能添加age属性
print(b.__dict__)