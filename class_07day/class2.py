# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/29 16:15
class Filed(object):
    # 一个类中只要出现以下三个方法的任意一个，那么该类就是描述器类

    def __get__(self, instance, owner):
        print("触发了__get__方法")

    def __set__(self, instance, value):
        print("触发了__set__方法")
        self.value = value
        print(self)
        print(instance)
        print(value)

    def __delete__(self, instance):
        print("触发了__delete__方法")
        print(self)
        self.value = None


class Model(object):
    name = 'toby'
    attr = Filed()  # 储存的是描述器对象，会覆盖类属性


m = Model()
m.name = '000'
m.attr = 100
print(m.name)
print(m.attr)
