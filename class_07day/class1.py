# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/29 16:15
# 自定义属性访问
class Test(object):
    def __init__(self):
        self.age = 18

    # 当我们访问属性的时候，如果属性不存在(出现AttrError)，该方法会被触发
    def __getattr__(self, item):
        print("-----这个是__getattr__")
        return 100

    # 查找属性的时候，第一时间触发该方法去找属性
    def __getattribute__(self, item):
        print("-----这个是__getattribute__方法")
        # return 999
        return super().__getattribute__(item)  # 会触发__getattr__方法

    def __setattr__(self, key, value):
        if key == 'age':
            super().__setattr__(key, 18)

        else:
            # 这个方法在给对象设置属性时触发
            print("-----设置属性的时候会触发这个方法-----")
            print(key)
            print(value)
            super().__setattr__(key, value)

    def __delattr__(self, item):
        print(item)
        # 这个方法在删除属性的时候会被触发
        print("-----__delattr__被调用-----")
        super().__delattr__(item)


t = Test()
t.time = 10
t.age = 999
del t.time  # 删除属性
print(t.time)
print(t.age)
