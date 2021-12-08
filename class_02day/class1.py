# @Time : 2021/12/4 10:58 
# @Author :jiale
# @File : class1.py 
# @Software: PyChar
import timeit
from collections import namedtuple  # 命名元组

print("--------------------运行时间--------------------")


def test_func_time():
    for i in range(10):
        pass


res = timeit.Timer(test_func_time).timeit(100)  # 运行100次的时间
print("运行100次的时间:{}".format(res))
print("--------------------运行时间--------------------")

print("--------------------命名元组--------------------")
#  命名元组,使得元组可以像列表一样取值
#  设定命名元组类型
# 第一个参数，名字 ，一般与命名元组一致，即student_info
# 第二个参数，列表，元组中的数据
student_info = namedtuple("info_tuple", ['name', 'age', 'gender'])
tu = student_info("toby", 25, "nan")  # 添加数据
print("命名元组中的数据:{}".format(tu))
print("命名元组中的name值:{0}，age值:{1}，性别值:{2}".format(tu.name, tu.age, tu.gender))
print("命名元组类型:{}".format(type(tu)))
print("--------------------命名元组--------------------")

print("--------------------字典和集合--------------------")
#  字典和集合{}，集合会自动去重
li1 = [1, 1, 1, 2, 2, 2, 3, 3, 3]  # 利用集合对列表去重
li2 = list(set(li1))  # 将列表转为集合
print("li2中的值是:{}".format(li2))
set1 = set()  # 定义一个空集合
set2 = {1, 2, 3, 3, 3, 4, 4, 4, 4}  # 定义一个集合
print("添加前集合中的值是:", set2)
#  集合添加数据
set2.add('toby')
print("添加后集合中的值是:{}".format(set2))
set2.remove('toby')  # 删除集合中的值“toby”
print("删除后集合中的值是:{}".format(set2))  # 空集合
set2.update({111, 222, 333, 444})  # 更新集合中的数据
print("更新后集合中的值是:{}".format(set2))
copy_data = set2.copy()
set2.clear()  # 清空集合
print("清空后集合中的值是:{}".format(set2))
print("copy_data中的值是:{}".format(copy_data))
dic = {}  # 定义一个空字典
print("--------------------字典和集合--------------------")
#  集合只能存储不可变的数据类型
#  可变和不可变元素(可哈希和不可哈希)
