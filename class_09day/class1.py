# -*- coding:utf-8 -*-
# Author:toby
# Date : 2022/1/6 16:24
#  可变数据类型 list dict set
#  不可变数据类型 数值类型 字符串 元组
#  小整数池 -5~256--->数值
#  大整数池(intern机制 ) 只存储包含标准字符(数字、字母、下划线)的字符串--->字符串
import copy

#  深浅拷贝通常在列表嵌套列表时使用
li = [1, 2, 3]
list1 = [11, 22, li]
list2 = copy.deepcopy(list1)
print(list2)
print(id(li))
print(id(list1))
print(id(list2))
# python垃圾回收机制：引用计数为主，标记-清除和分代收集两种机制为辅的策略
