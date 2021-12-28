# -*- coding:utf-8 -*-
# Author:toby
# Date : 2021/12/23 17:16
# with open('test.txt', 'w+', encoding='utf8') as f:
#     f.write('最近崩溃好多啊')


# with后面跟的是一个上下文管理器对象
class MyOpen(object):  # 自己定义一个文件上下文管理器
    # 文件操作的上下文管理器
    def __init__(self, filename, open_method, encoding='utf8'):
        self.filename = filename
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):  # 文件操作
        self.f = open(self.filename, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):  # 文件关闭
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.f.close()


with MyOpen('test.txt', 'w') as f:
    content = f.write("我自横刀向天笑111,,,")
with MyOpen('test.txt', 'r') as f:
    read=f.read()
    print(read)
