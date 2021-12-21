# @Time : 2021/12/21 21:55 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
# 重写__str__和__repr__方法时，必须记得写return
# 重写__str__和__repr__方法时，return返回的必须是一个字符串
class MyClass(object):
    def __init__(self, name):  # 设置初始化属性
        self.name = name

    def __str__(self):
        print("---str触发了")
        return 'ggg'
        # return self.name

    def __repr__(self):
        print("repr被触发")
        return '<MyClass.object-{}>'.format(self.name)

    def __call__(self, *args, **kwargs):
        # 在像函数一样调用时触发对象
        print("----------call---------")


m = MyClass('toby')
print(m)
str(m)
format(m)  # 触发str方法
res = repr(m)
print(res)
m()

# 使用str函数或者print打印对象时会优先触发str方法，没有定义str方法的情况下，会再去找repr方法，如果都没有，才会去找父类的str方法
# 使用str方法或者交互环境下输入变量，会先找自身的repr方法，自身没有repr方法，会再去找父类的repr方法
