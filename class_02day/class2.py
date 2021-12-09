# @Time : 2021/12/5 22:40 
# @Author :jiale
# @File : class2.py 
# @Software: PyCharm
print("--------------------列表推导式--------------------")

# 需求：生成100个随机的url
# 1、使用循环
urls1 = []  # 定义一个空列表
for i in range(1, 101):
    url = 'www.baidu.com:8080/page{}'.format(i)
    urls1.append(url)
print("url1中的数据:{}".format(urls1))
# 2、使用列表推导式
urls2 = ['www.baidu.com:8080/page{}'.format(i) for i in range(1, 101)]
print("url2中的数据:{}".format(urls2))
print("--------------------列表推导式--------------------")
print("--------------------字典推导式--------------------")
#  字典推导式
dict1 = {i: '编号' for i in range(10)}
print("dict1中的数据:{}".format(dict1))
print("--------------------字典推导式--------------------")
print("--------------------生成器表达式--------------------")
# 生成器表达式
tu = (i for i in range(10))  # 生成器对象
print("tu:{}".format(tu))
print("tu生成器中下一个值:{}".format(next(tu)))
print("tu生成器中下一个值:{}".format(next(tu)))


def gen_fun():
    yield 100  # 通过yield定义生成器
    print("hello toby")
    yield 1000


res = gen_fun()  # 返回生成器对象
print("res生成器中下一个值:{}".format(next(res)))
print("res生成器中下一个值:{}".format(next(res)))
print("--------------------生成器表达式--------------------")
print("--------------------迭代器--------------------")
# 可迭代对象：可以for循环遍历的都是可迭代对象,内部只实现了__iter__方法
li1 = [1, 2, 3, 4]  # 定义一个列表
li2 = iter(li1)  # iter()  __iter__
#  迭代器  内部实现了__iter__方法和__next__方法
print("li1可迭代对象中的下一个值:{}".format(next(li2)))
print("li1可迭代对象中的下一个值:{}".format(next(li2)))
print("li1可迭代对象中的下一个值:{}".format(next(li2)))
print("li1可迭代对象中的下一个值:{}".format(next(li2)))
#  print("li1可迭代对象中的下一个值:{}".format(next(li2)))  # 超出可迭代范围，报错
print("--------------------迭代器--------------------")
print("--------------------生成器--------------------")


#  生成器是迭代器的一种
#  生成器相比迭代器多了几种方法  send close throw
#  tu.send()  #  与生成器交互
def gen_test():
    for i in range(1, 5):
        se = yield i
        print('se的值:', se)


g = gen_test()
print("g生成器中的值:{}".format(g))
print("g生成器中的下一个值:{}".format(next(g)))
print("g生成器中的下一个值:{}".format(next(g)))
print("g生成器中的下一个值:{}".format(next(g)))


#  生成器的三个方法 send close throw
# send
def gen_test_01():
    j = 0
    for i in range(5):
        j = yield i
        print(j)


f = gen_test_01()
print("f生成器中的值:{}".format(f))
print("f生成器中的下一个值:{}".format(next(f)))
print("f生成器中的下一个值:{}".format(next(f)))
print("f生成器中的下一个值:{}".format(next(f)))
f.send(999)  # 传入数据
print("f生成器中的下一个值:{}".format(next(f)))
f.throw(ValueError, "hello toby")
f.close()  # 关闭生成器
#  在生成器内部主动引发一个异常  参数：异常类型 异常信息
print("--------------------生成器--------------------")
