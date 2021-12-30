# @Time : 2021/12/29 21:42 
# @Author :jiale
# @File : class1.py 
# @Software: PyCharm
# 元类
# python中内置的元类，type
# 空元组  ()
# 元组中只有一个参数  (obj,)
# 利用元类直接创建类
def func(self):
    print('-----这个时self-----')


# type创建类需要三个参数
# 1、第一个：类名-->str
# 2、第二个：继承的父类-->tuple
# 3、第三个：字典-->dict,键值对的形式表示属性
test = type('test', (object,), {'attr': '100', '__attr': '200', 'func1': func})
print(test)
print(test.__dict__)
t = test()
t.func1()


class Test1(object):
    attr = 100
    __attr2 = 200


print(Test1)
