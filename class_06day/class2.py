# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/23 17:17
class MyClass(object):
    def __init__(self, data):  # 初始化函数，需要传入data
        self.data = data

    def __str__(self):
        print("---------触发了__str__方法---------")
        return self.data

    def __add__(self, other):  # 加法
        print("---------触发了__add__方法---------")
        print("self：", self)
        print("other：", other)
        return self.data + other.data

    def __sub__(self, other):
        print("---------触发了__sub__方法---------")
        return self.data.replace(other.data, '')


if __name__ == '__main__':
    s1 = MyClass('sss111')
    s2 = MyClass('sss222')
    print(MyClass(s1 + s2))
    s3 = MyClass(s1 + s2)
    print("s3的值：", s3)
    print("s3-s1的值：", s3 - s1)