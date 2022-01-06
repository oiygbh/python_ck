# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/6 16:14
class BoolFiled(object):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):  # 类型限制
            self.value = value
        else:
            raise ValueError

    def __delete__(self, instance):
        self.value = None


class UserModel(object):
    # 假设这个是模型类
    name = BoolFiled()  # 只能赋值为布尔类型


if __name__ == '__main__':
    b = BoolFiled()
    b.name = True
    print(b.name)
"""
1、object.__getattr__方法
如果被访问（查找）属性不存在时会被触发
2、object__getattribute__方法
访问（查找）属性时，第一时间触发__getattribute__方法查找属性
3、object__setattr__方法
设置属性时触发__setattr__方法
4、object__delattr__方法
在删除属性时会触发
"""