# @Time : 2021/12/29 22:04 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
# 自定义元类
# 自定义元类，必须继承与type
class MyMetaClass(type):
    """
    自定义元类，将类的所有属性名变为大写
    """

    # 重写new方法
    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        print('最基础的自定义元类')
        # 遍历字典键值对
        for k, v in attr_dict.items():
            attr_dict.pop(k)
            attr_dict[k.upper()] = v
        attr_dict['__slots'] = ['name', 'age', 'gender']

        return super().__new__(cls, name, bases, attr_dict)


# 通过自定义的元类来创建类
class Test(metaclass=MyMetaClass):  # 指定继承的父类，默认时object
    name = 'toby'
    age = 99
    gender = '男'


# 父类指定元类，子类可以继承父类指定的元类
class MyClass(Test):
    pass


print(type(MyClass))
# print(Test.name)
print(type(Test))
# 定义一个类，通过元类让该类的类属性变成大写字母
t = Test()
print(t.__dict__)
# print(Test.__dict__)  # 所有类属性
