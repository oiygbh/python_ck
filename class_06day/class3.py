# @Time : 2021/12/25 14:31 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
#  python函数的参数没有类型限制
#  多态
class Base(object):
    def run(self):
        print("-----base-----run-----:慢慢走路")


class Cat(Base):
    def run(self):
        print("-----base-----run-----:会爬树")

# 当需要新增功能，只需要新增一个Base的字类实现run()方法，就可以在原有的基础上
# 进行功能扩展，这就是著名的“开放封闭原则”
# 对扩展开放:允许新增Base子类
# 对修改封闭:不需要修改依赖Base类型的run()等函数
class Dog(Base):
    def run(self):
        print("-----base-----run-----:跑的特别快")


class Pig(Base):
    pass


b_obj = Base()
c_obj = Cat()
d_obj = Dog()
p_obj = Pig()
# python中的函数参数没有类型限制
# 子类的对象是属于父类的类型
print(isinstance(c_obj, Base))
print(isinstance(c_obj, Base))


def func(base_obj):
    base_obj.run()


func(b_obj)
func(c_obj)
func(d_obj)
func(p_obj)
