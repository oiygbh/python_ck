# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/21 17:09
def test_01(a):
    print("666")

    def test1():
        print(a * 9)

    return test1()


test_01(5)


def test_02(a):
    print("666")

    def test1():
        print(a * 9)

    return test1


a = test_02(8)
a()
