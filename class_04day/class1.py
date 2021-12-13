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
def func(num):
    def count_book():
        print(num)
        print("哈哈哈哈")

    return count_book()


func(1999)


#  装饰器，不修改现有代码，添加新功能
#  开放封闭功能
def index():
    print("这是网站首页")


index()
