# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/14 16:16
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#  方法1
count = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if i == j or j == k or i == k:
#                 continue
#             else:
#                 print(i, j, k)
#                 count += 1
# print(count)
#  方法2
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)
                count += 1
print(count)
