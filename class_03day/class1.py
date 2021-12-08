# @Time : 2021/12/8 22:02 
# @Author :jiale
# @File : class1.py 
# @Software: PyCharm
#  迭代器、可迭代对象、生成器
from collections import Iterator, Iterable, Generator
#  递归函数：在函数中调用函数本身
#  案例需求一：通过递归函数实现任意数的阶乘

def fun(n):
    if n == 1:  # n = 1 是递归临界点，不再调用自身函数的条件
        return 1
    else:
        return n * fun(n - 1)


fun(5)
# 纯函数
# 概念：一个函数的返回结果只依赖于他的参数，并且在执行过程中没有副作用，把这个函数叫做纯函数
# 原则
# 1、变量只在函数作用域内获取，作为函数的参数传入
# 2、不会产生副作用，不会改变被传入的数据或其他数据（全局变量）
# 3、相同的输入保证相同的输出
