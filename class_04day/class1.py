# @Time : 2021/12/13 21:55 
# @Author :jiale
# @File : class3.py 
# @Software: PyCharm
#  闭包条件
#  1、函数中嵌套函数
#  2、外层函数返回内层嵌套函数名
#  3、内层嵌套函数有引用外层的一个非全局变量
#  作用
#  4、实现书局锁定，提高稳定性
# def func(num):
#     def count_book():
#         print(num)
#         print("哈哈哈哈")
#
#     return count_book()


# func(1999)


def login(func):  # func是被装饰函数
    def fun():
        username = "toby"
        password = "123456"
        user = input("请输入账号：")
        pwd = input("请输入密码：")
        if user == username and pwd == password:
            func()
        else:
            print("账号或者密码错误")

    return fun


#  装饰器，不修改现有代码，添加新功能
#  开放封闭功能
@login  # @login：语法糖 -->index=login(index)
def index():
    print("这是网站首页")



# print(index.__closure__)
index()  # 等于login(index)
# 装饰器应用场景
#1、登录验证
#2、函数运行时间统计
#3、执行函数之前的准备工作
#4、执行函数之后的清理工作