# @Time : 2021/12/15 22:18
# @Author :jiale
# @File : class_04_homework.py
# @Software: PyCharm
"""
1、一个完整的闭包必须满足哪几个条件
2、定义一个计算函数运行时间的装饰器(计算时间使用time模块实现)
3、编写装饰器，为多个函数加上认证的功能(用户的账号密码来自文件)，要求登录成功一次，后续的函数都无须再输入账号和密码
"""
# 2、
import time


# def wrapper(func):
#     def count_time(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         end_tine = time.time()
#         print("函数运行的时间为:{:.5f}".format(start_time - end_tine))
#
#     return count_time()


with open('user.txt') as f:
    users = eval(f.read())
print(users)
print(users['user'])
print(users['pwd'])
print(users['token'])

def login_check(func):
    """
    登录验证装饰器
    :param func_01: type；functions
    :return:
    """

    def ado():
        if users["token"] is False:  # 判断token是否为false
            print("----------登录页面----------")
            username = input("输入账号：")
            password = input("输入密码：")
            # 登录校验
            if users["user"]==username and users["pwd"]==password:
                users["token"] == True  # 修改token值
                func()  # 调用装饰器函数
        else:
            func()  # token值为True直接调用函数
    return ado


@login_check
def index():
    print("这里是网站首页")


@login_check
def page1():
    print("这里是page1页面")


@login_check
def page2():
    print("这里是page2页面")


if __name__ == '__main__':
    index()
    page1()
    page2()
