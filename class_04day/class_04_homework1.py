# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/20 9:25


# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
with open('user.txt') as f:
    users = eval(f.read())
print(users)


def login_check(func):
    """
    登录验证的装饰器
    :param func: type:functions
    :return:
    """

    def ado():
        if not users['token']:  # 判断token值是否为False
            print('------------------登录页面------------------')
            username = input("账号：")
            password = input("密码：")
            # 登录校验
            if users["user"] == username and users["pwd"] == password:
                users["token"] = True  # 修改token的值
                func()  # 调用被装饰器的函数
        else:
            func()  # token值为True直接调用函数

    return ado


@login_check
def index():
    print("这个是index首页！")


@login_check
def page1():
    print("这个是page1页面！")


@login_check
def page2():
    print("这个是page2页面！")


if __name__ == '__main__':
    index()
    page1()
    page2()
