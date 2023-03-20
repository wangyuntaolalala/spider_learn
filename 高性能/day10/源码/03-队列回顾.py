#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-队列回顾.py    
# Author :   柏汌  

# 队列
from queue import Queue
q = Queue(maxsize=3)

item = {}
q.put(item)
print(q.qsize())

q.put('222')
q.put_nowait(item)  # 不等待直接放入   如果队列已满会报错

print(q.qsize())
# print(q.get())
# q.get_nowait()   # 不等待直接取  队列为空报错
q.task_done()
print(q.get())
print(q.qsize())
q.join()   # 队列维持了一个计数 计数不为0的时候会让主线程等待 , 这个可以联系之前的线程join方法

# todo:get 和task_done 一起使用才会减一
# todo:通过put提交数据的时候    计数   会+1   get取数据    不会-1








