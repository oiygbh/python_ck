# @Time : 2021/12/13 21:24 
# @Author :jiale
# @File : class_03_homework.py 
# @Software: PyCharm
import sys
sys.setrecursionlimit(3000)  # 修改默认递归次数，默认是1000，避免栈溢出
# 1、使用递归实现斐波那契数列中相应位置的值
"""
1
1
2
3
5
"""


def fixb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fixb(n - 1) + fixb(n - 2)


print(fixb(10))
# 2、兔子题
# 3、小明有100元钱，A类书籍5元一本，B类书籍3元一本，C类书籍1元2本，请用程序计算出小明
# 一共有多少种买法
# 方法1
money = 100
book = 100
count = 0
for a in range(int(money / 5)):
    for b in range(int(money / 3)):
        for c in range(int(money / 0.5)):
            if a * 5 + b * 3 + c * 0.5 <= 100 and a + b + c == 100:
                print(a, b, c)
                count += 1
print(count)
# 递归实现
# python递归次数的最大限制是1000次
