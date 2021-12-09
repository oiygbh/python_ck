# @Time : 2021/12/8 22:39 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
#  常用的内置函数
#  map函数
#  filter()
#  zip函数
#  迭代器、可迭代对象、生成器
# from collections import Iterator, Iterable, Generator
from functools import  partial  # 偏函数

def fun(n):
    return n < 10


# filter过滤函数
# 第一个参数是 函数
# 第二个参数是可迭代对象
li1 = [1, 2, 3, 444, 5, 6, 7, 88, 99, 43]
res = filter(fun, li1)
print(list(res))  # 用于过滤
li2 = iter(li1)  # 将列表转换迭代器
li3 = (i for i in range(5))  # 生成器
# print(isinstance(li1, Iterable))  # 判断是否是可迭代对象
# print(isinstance(li2, Iterable))  # 判断是否是可迭代对象
# print(isinstance(li3, Iterable))  # 判断是否是可迭代对象
# map内置函数，将可迭代对象中的数据迭代出来，一个一个传到函数中调用，将返回结果放到新的对象中
res2 = map(fun, li1)
print(list(res2))
# zip函数，打包
res3 = zip([1, 2, 3], [11, 22, 33])
print(res3)  # 返回可迭代对象
print(dict(list(res3)))
dict1 = {'key1': '1', 'key2': 2, 'key3': '3'}
print(list(dict1.items()))


# 匿名函数
def func(a, b):
    return a + b


(lambda a, b: a + b)(1, 2)  # 使用场景，节约内存
res4 = lambda a, b: a + b  # 命名匿名函数，返回两个数之和
# 匿名函数适用场景：简单的函数定义，只有一个表达式
print(res4(11, 22))  # 调用匿名函数
res5 = filter(lambda x: x < 10, li1)  # lambda常用场景
print(list(res5))
li4 = [(lambda x: x % 5 == 0) for i in range(10)]
print(li4)
# 三目运算
a = 100
print(100) if a >100 else print(10)
li5=[1, 2, 3, 5, 6, 7]
li6=[1, 2, 3, 5, 6, 7]
li7=[1, 2, 3, 5, 6, 7]
li8=[1, 2, 3, 5, 6, 7]
# 偏函数
filter2 = partial(filter,lambda x:x>5)
res6 = filter2(li5)
print(list(res6))