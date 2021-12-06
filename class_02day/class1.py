# @Time : 2021/12/4 10:58 
# @Author :jiale
# @File : class1.py 
# @Software: PyChar
import timeit
from collections import namedtuple  # 命名元组

print("运行时间")


def func():
    for i in range(10):
        print(i)


res = timeit.Timer(func).timeit(100)  # 运行100次的时间
print(res)
print("命名元组")
#  命名元组,使得元组可以像列表一样取值
# tu = ("toby", 25, "nan")
#  设定命名元组类型
student_info = namedtuple("info_tuple", ['name', 'age', 'gender'])  # 第一个参数  名字  第二个参数 列表
tu = student_info("toby", 25, "nan")  # 添加数据
print(tu)
print(tu.name, tu.age, tu.gender)
print(type(tu))
print("字典和集合")
#  字典和集合{}，集合会自动去重
li1 = [1, 1, 1, 2, 2, 2, 3, 3, 3]  # 利用集合对列表去重
li2 = list(set(li1))
print(li2)
se = set()  # 定义一个空集合
set1 = {1, 2, 3, 3, 3, 4, 4, 4, 4}  # 定义一个集合
print(set1)
#  集合添加数据
se.add('toby')
print(se)
se.remove('toby')
print(se)  # 空集合
se.update({111, 222, 333, 444})  # 更新集合中的数据
print(se)
se.clear()  # 清空集合
se.copy()  # 复制集合
dic = {}  # 定义一个空字典
#  集合只能存储不可变的数据类型
#  可变和不可变元素(可哈希和不可哈希)
