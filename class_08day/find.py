# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/6 16:23
class BaseFiled(object):
    pass


class CharFiled(BaseFiled):
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


class IntFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):  # 类型限制
            self.value = value
        else:
            raise TypeError("name只能是整数")

    def __delete__(self, instance):
        self.value = None


class BoolFiled(BaseFiled):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):  # 类型限制
            self.value = value
        else:
            raise ValueError

    def __delete__(self, instance):
        self.value = None
