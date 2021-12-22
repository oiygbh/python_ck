# @Time : 2021/12/22 21:50 
# @Author :jiale
# @File : class1.py 
# @Software: PyCharm
# with open('test.txt', 'w+', encoding='utf8') as f:
#     f.write('最近崩溃好多啊')


# with后面跟的是一个上下文管理器对象
class MyOpen(object):
    # 文件操作的上下文管理器
    def __init__(self, filename, open_method, encoding='utf8'):
        self.filename = filename
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):  # 文件操作
        self.f = open(self.filename, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):  # 文件关闭
        print(exc_tb)
        print(exc_val)
        print(exc_val)
        self.f.close()


with MyOpen('test.txt', 'r') as f:
    content=f.read()
    print(content)
with MyOpen('test1.txt', 'w') as f:
    pass
    print(f)
