# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/27 10:24
class Test():
    attr1 = 1000  # 公有属性
    _attr2 = 3000  # 私有属性，单下划线开头
    __attr3 = 4000  # 私有属性，双下划线开头


c = Test()  # 类的实例对象
# 类属性可以通过类和实例对象去访问
print("通过类访问attr1公有属性:", Test.attr1)  # 通过类访问
print("通过实例对象访问attr1公有属性::", c.attr1)  # 通过实例对象访问
# 访问单下划线_开头私有属性
print("通过类访问_attr2私有属性:", Test._attr2)  # 通过类访问
print("通过实例对象访问_attr2私有属性:", c._attr2)
# 访问双下划线__开头私有属性
# 双下划线__开头的私有属性，对外不能直接访问，对外改了一个名字
# 在原有的名字前面加了 _类名
print("通过类访问__attr3私有属性:", Test._Test__attr3)
print("通过实例对象访问__attr3私有属性:", c._Test__attr3)
# 查看类的所有属性
print("类的所有属性:", Test.__dict__)


# 类调用__dict__属性，返回类属性和方法的字典
# 类实例调用__dict__属性，返回的是类相关的属性和方法
#  私有属性的继承问题,私有属性可以继承
class A(Test):  # 继承Test类的子类
    name = 'toby'


a = A()  # A的实例对象
print("子类的对象访问父类的公有属性:", a.attr1)
print("子类的对象访问父类的私有属性:", a._attr2)
print("子类的对象访问父类的私有属性:", a._Test__attr3)
