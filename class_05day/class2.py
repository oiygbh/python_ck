# @Time : 2021/12/20 21:55 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
# 面向对象之魔术方法
# __init__魔术方法

class MyClass(object):
    def __init__(self, name):  # 设置初始化属性
        self.name = name

    def __new__(cls, *args, **kwargs):  # 重写new方法
        print("这个是new方法")
        # return super().__new__(cls)  #  子类调用父类方法
        # return object.__new__(cls)


m = MyClass('toby')
# print(m)
# print(m.name)


# __new__方法，在__init__之前执行
#  单例模式，类只能被实例化一次

class MyTest(object):
    instance = None  # 设置一个类属性，用来记录该类有没有创建过对象

    def __new__(cls, *args, **kwargs):
        if not cls.instance:  # if MyTest.instance
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance
#  装饰器实现单例模式
t1=MyTest()
t1.name='toby'
t2=MyTest()
print(t2.name)
t2.age='19'
print(t2.age)
print(id(t1))  #  内存地址
print(id(t2))  #  内存地址