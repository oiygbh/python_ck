# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/13 14:57
#  常用的内置函数
#  map函数
#  filter()
#  zip函数
#  迭代器、可迭代对象、生成器
from collections import Iterator, Iterable, Generator
from functools import partial  # 偏函数

print("--------------------filter内置函数--------------------")


def test_filter(n):
    return n < 10


# filter过滤函数
# 第一个参数是 函数
# 第二个参数是可迭代对象
li1 = [1, 2, 3, 444, 5, 6, 7, 88, 99, 43]
res = filter(test_filter, li1)
print("列表list1中小于10的值:{}".format(list(res)))  # 用于过滤
li2 = iter(li1)  # 将列表转换迭代器
li3 = (i for i in range(5))  # 生成器
print("判断li1是否是可迭代对象:{}".format(isinstance(li1, Iterable)))  # 判断是否是可迭代对象
print("判断li2是否是可迭代对象:{}".format(isinstance(li2, Iterable)))  # 判断是否是可迭代对象
print("判断li3是否是可迭代对象:{}".format(isinstance(li3, Iterable)))  # 判断是否是可迭代对象
print("--------------------filter内置函数--------------------")
print("--------------------map内置函数--------------------")
# map内置函数，将可迭代对象中的数据迭代出来，一个一个传到函数中调用，将返回结果放到新的对象中
res2 = map(test_filter, li1)
print(list(res2))
print("--------------------map内置函数--------------------")
print("--------------------zip内置函数--------------------")
# zip函数，打包
res3 = zip([1, 2, 3], [11, 22, 33])
print(res3)  # 返回可迭代对象
print(dict(list(res3)))
dict1 = {'key1': '1', 'key2': 2, 'key3': '3'}
print(list(dict1.items()))

print("--------------------zip内置函数--------------------")

print("--------------------匿名函数和偏函数--------------------")


# 匿名函数
def test_anonymous(a, b):
    return a + b


(lambda a, b: a + b)(1, 2)  # 使用场景，节约内存
res4 = lambda a, b: a + b  # 命名匿名函数，返回两个数之和
# 匿名函数适用场景：简单的函数定义，只有一个表达式
print("调用匿名函数:{}".format(res4(11, 22)))  # 调用匿名函数
res5 = filter(lambda x: x < 10, li1)  # lambda常用场景
print(list(res5))
li4 = [(lambda x: x % 5 == 0) for i in range(10)]
print("li4中为质数的是:{}".format(li4))

# 三目运算
a = 100
print(100) if a > 100 else print(10)
li5 = [1, 2, 3, 5, 6, 7]
li6 = [1, 2, 3, 5, 9]
li7 = [1, 2, 3, 5, 11, 17]
li8 = [1, 2, 3, 5, 16, 27]

# 偏函数
filter2 = partial(filter, lambda x: x > 5)
res6 = filter2(li5)
print("li5、6、7、8中大于5的数:{}".format(list(res6)))
print("--------------------匿名函数和偏函数--------------------")
