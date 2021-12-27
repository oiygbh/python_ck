# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/21 16:39
# 面向对象之魔术方法
# __init__魔术方法
print("--------------------__init__魔术方法--------------------")


class MyClass(object):
    def __init__(self, name):  # 设置初始化属性
        self.name = name

    def __new__(cls, *args, **kwargs):  # 重写new方法
        print("这个是new方法")
        # return super().__new__(cls)  #  子类调用父类方法
        return object.__new__(cls)


m = MyClass('toby')  # 类实例化
print(m)
print(m.name)
# __new__方法，在__init__之前执行
print("--------------------__init__魔术方法--------------------")
print("--------------------单例模式--------------------")


# __new__方法，在__init__之前执行
#  单例模式，类只能被实例化一次

class MyTest(object):
    __instance = None  # 设置一个类属性，用来记录该类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:  # if MyTest.instance
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance


print("--------------------单例模式--------------------")
if __name__ == '__main__':
    #  装饰器实现单例模式
    t1 = MyTest()  # 类实例t1
    t1.name = 'toby'  # 设置类属性name，值toby
    print("t1属性name值:", t1.name)  # 类属性
    t2 = MyTest()  # 类实例t2
    print(t2.name)  # t2直接调用t1的属性值
    t2.age = '19'  # 设置类属性age，值19
    print("t2属性age值:", t2.age)
    print(id(t1))  # 内存地址
    print(id(t2))  # 内存地址
