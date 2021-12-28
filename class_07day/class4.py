# @Time : 2021/12/28 22:05 
# @Author :jiale
# @File : class4.py 
# @Software: PyCharm
# 经典类，继承：instance类型，python2
class MyClass():
    pass


# 新式类，继承：obiect,python3
class Test():
    pass


t = Test()
print(type(t))
print(type(Test))
print(type(type))
# type；python中所有的类都是通过type来创建出来的，type是元类
# object：python3中所有类的顶级父类
