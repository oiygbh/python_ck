# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/21 15:45
# with open('user.txt') as f:
#     users = eval(f.read())
# print(users)
from class_04_homework0 import DoExcel

test_data = DoExcel.read_case('testdata.xlsx', 'user')
print(test_data)
for i in test_data:
    username = i['username']
    password = i['password']
    token = i['token']
    print(i['username'])
    print(i['password'])
    print(i['token'])


def login_check(func):
    """
    登录验证的装饰器
    :param func: type:functions
    :return:
    """

    def ado():
        if not token:  # 判断token值是否为False
            print('------------------登录页面------------------')
            username_input = input("账号：")
            password_input = input("密码：")
            # 登录校验
            if username_input == username and password_input == password:
                DoExcel.write_back('testdata.xlsx', 'user', 2, 3, 'True')
                # users["token"] = True  # 修改token的值
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
