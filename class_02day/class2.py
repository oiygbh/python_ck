# @Time : 2021/12/5 22:40 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
urls1 = []
for i in range(1, 101):
    url = 'page{}'.format(i)
    urls1.append(url)
#  print(urls1)
# 列表推导式
urls2 = ['page{}'.format(i) for i in range(1, 101)]
#  print(urls2)
#  字典推导式
dict1 = {i: 'i' for i in range(10)}
print(dict1)
# 生成器表达式
tu = (i for i in range(10))  # 生成器对象

#  print(next(tu))


# def gen_fun():
#     yield 100  # 通过yield定义生成器
#     print("hello toby")
#     yield 1000
#
#
# res = gen_fun()  # 返回生成器对象
# print(next(res))
# print(next(res))


# 列表
# 可迭代对象：可以for循环遍历的都是可迭代对象,内部只实现了__iter__方法
li1 = [1, 2, 3, 4]
li2 = iter(li1)  # iter()  __iter__
#  迭代器  内部实现了__iter__方法和__next__方法
print(next(li2))  # __next__


#  生成器是迭代器的一种
#  生成器相比迭代器多了几种方法  send
#  tu.send()  #  与生成器交互
def gen():
    for i in range(1, 5):
        se = yield i
        print('se的值:', se)


g = gen()
print(next(g))
print(g.send(100))
print(next(g))
