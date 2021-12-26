# @Time : 2021/12/21 22:29 
# @Author :jiale
# @File : class_05_homework.py 
# @Software: PyCharm

# 1、通过装饰器实现单例模式，只要任意一个类使用该装饰器装饰，那么就会变成一个单例模式的类
def single(cls):
    instance = {}

    def fun(*args, **kwargs):
        if cls in instance:
            return instance[cls]
        else:
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]
        return fun


@single  # Test=single(Test)
class Test:
    pass


T1 = Test


# 2、通过类实现一个通用装饰器，既可以装饰函数，也可以装饰类，既可以装饰有参数的，也可以装饰无参数的
# 通过类实现装饰器__call__方法，调用类时会自动调用__call__方法
class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("这个是装饰器里面的功能")
        self.func()
        print("装饰器里面的功能")


@Decorator  # test_01=Decorator(test_01)
def test_01():
    print("原来的功能函数")


test_01()
# 3、请描述__new__、__str__、__repr__、__call__分别在什么情况下会被调用
# __new__，创建实例对象时被调用
# __str__，print打印时会被触发，format也会被触发，str转换时也会触发
# __repr__，在交互环境下输入对象会被触发，repr内置函数也会触发
# __call__，对象在被调用时会触发
