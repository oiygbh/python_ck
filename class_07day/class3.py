# @Time : 2021/12/28 21:36 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
# 描述器
class CharFiled:
    def __init__(self, max_lenght=20):
        self.max_lenght = max_lenght

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):  # 类型限制
            if len(value) <= self.max_lenght:
                self.value = value
            else:
                raise ValueError("字符串长度应该在{}以内".format(self.max_lenght))
        else:
            raise TypeError("name只能是字符串")

    def __delete__(self, instance):
        self.value = None
class IntFiled:


    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):  # 类型限制
            self.value = value
        else:
            raise TypeError("name只能是整数")

    def __delete__(self, instance):
        self.value = None

class UserModel(object):
    # 假设这个是模型类
    name = CharFiled(max_lenght=20)  # 只能赋值为字符串
    pwd = CharFiled(max_lenght=40)
    age = IntFiled()


m = UserModel()
# m.name = 999
m.name = '99900000000'
m.pwd = '76gjkmvvg'
m.age='18'
print(m.name)
print(m.pwd)
print(m.age)