# @Time : 2022/1/10 22:12 
# @Author :jiale
# @File : class4.py 
# @Software: PyCharm
# 队列
import queue

# 1、先入先出
q = queue.Queue(10)  # 创建一个队列，长度为3，默认无限制
# 往队列添加数据
q.put(1)
q.put(11)
q.put(111)
# q.put(1111)
# q.put(1111, block=False)  # 往队列添加数据，不等待，如果队列已满，会报错
# q.put_nowait(1111)  # 往队列添加数据，不等待，如果队列已满，会报错
# 获取队列中的数据

# print(q.get())  # 获取数据
# print(q.get())
# print(q.get())
# print(q.get(block=False))  # 获取队列数据，不等待，如果队列为空，会报错
# print(q.get_nowait())  # 获取队列数据，不等待，如果队列为空，会报错
print(q.qsize())  #  获取队列中的任务数
# q.put(12)
print(q.full())  # 判断队列是否已满
q.task_done()  # 任务完成时调用
q.task_done()
q.task_done()
print(q.empty())  # 判断队列是否为空
# join 判断队列中的任务是否执行完毕
print(q.join())
# 2、后入先出
q2=queue.LifoQueue()  # 后入先出,方法与先入先出一样
q2.put(1)
q2.put(11)
q2.put(111)
print(q2.get())

# 3、优先级，方法与先入先出一样
q3=queue.PriorityQueue()
q3.put((1,'jjj'))
q3.put((2,'gggg'))
q3.put((3,'hhhh'))
q3.put((4,'cccc'))
print(q3.get())  # 优先级低的先出