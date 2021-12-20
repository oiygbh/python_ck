# @Time : 2021/12/20 21:55 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
# 面向对象之魔术方法
# __init__魔术方法
class MyClass(object):
    def __init__(self,name):  # 设置初始化属性
        self.name = name
    def __new__(cls, *args, **kwargs):  #  重写new方法
        print("这个是new方法")
        # return super().__new__(cls)  #  子类调用父类方法
        # return object.__new__(cls)

m = MyClass('toby')
#print(m)
print(m.name)
# __new__方法，在__init__之前执行