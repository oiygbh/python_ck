# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/14 15:57
#  闭包条件
#  1、函数中嵌套函数
#  2、外层函数返回内层嵌套函数名
#  3、内层嵌套函数有引用外层的一个非全局变量
#  作用：实现数据锁定，提高稳定性
print("--------------------闭包--------------------")


def closure(num):
    def count_book():
        print(num)
        print("哈哈哈哈")

    return count_book()


closure(1999)
print("--------------------闭包--------------------")

print("--------------------简单装饰器--------------------")


def login(decorator):  # decorator是被装饰函数
    def fun_01():
        username = "toby"
        password = "123456"
        user = input("请输入账号：")
        pwd = input("请输入密码：")
        if user == username and pwd == password:
            decorator()
        else:
            print("账号或者密码错误")

    return fun_01


#  装饰器，不修改现有代码，添加新功能
#  开放封闭功能
@login  # @login：语法糖 -->index=login(index)
def index():
    print("这是网站首页，被装饰的函数")


print(index.__closure__)
print("--------------------简单装饰器--------------------")
index()  # 等于login(index)
# 装饰器应用场景
# 1、登录验证
# 2、函数运行时间统计
# 3、执行函数之前的准备工作
# 4、执行函数之后的清理工作
