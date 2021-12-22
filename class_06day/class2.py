# @Time : 2021/12/22 22:19 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
class MyClass(object):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):
        print("触发了add方法")
        print("self", self)
        print("other", other)
        return self.data + other.data

    def __sub__(self, other):
        return self.data.replace(other.data,'')


s1 = MyClass('sss111')
s2 = MyClass('sss222')
print(MyClass(s1 + s2))
s3 = MyClass(s1 + s2)
print(s3 - s1)
