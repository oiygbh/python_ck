# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/22 10:47
# 重写__str__和__repr__方法时，必须记得写return
# 重写__str__和__repr__方法时，return返回的必须是一个字符串
print("--------------------__str__和__repr__方法--------------------")


class MyClass(object):
    def __init__(self, name):  # 设置初始化属性
        self.name = name

    def __str__(self):
        print("-----str-----触发")
        # return 'ggg'
        return self.name

    def __repr__(self):
        print("-----repr-----被触发")
        return '<MyClass.object-{}>'.format(self.name)

    def __call__(self, *args, **kwargs):
        # 在像函数一样调用时触发对象，可以用来写类装饰器
        print("----------call---------")


# 使用str函数或者print打印对象时会优先触发str方法，没有定义str方法的情况下，会再去找repr方法，如果都没有，才会去找父类的str方法
# 使用str方法或者交互环境下输入变量，会先找自身的repr方法，自身没有repr方法，会再去找父类的repr方法
print("--------------------__str__和__repr__方法--------------------")
if __name__ == '__main__':
    m = MyClass('toby')
    print(m)  # 触发__str__方法
    str(m)  # 触发__str__方法
    format(m)  # 触发__str__方法
    res = repr(m)
    print(res)
    m()  # 直接触发类的__call__方法
