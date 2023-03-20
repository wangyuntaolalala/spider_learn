#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/11/1 18:29
# @Author : Wangyt

"""
高性能异步爬虫，联系之前的项目，如果对速度有要求，子步骤有阻塞且各个步骤串行的话，就可以考虑异步
联系grequests模块，
异步爬虫的方式：
    -多线程、多进程：
        好处：可以为相关阻塞的操作单独开启线程或者进程
        弊端：无法无限制地开启多线程、多进程（不建议这种）
    - 线程池、进程池：（适当的使用）
        好处：降低os对县城或者进程创建和销毁的频率
        弊端：池中线程或者进程的数量其实是有上限的,如果阻塞的操作的数量，远远多于可迭代对象（可以理解为操作对象的数量）的数量的时候，线程池的效果就没那么好了
    -单线程+异步协程（推荐）：

"""
import time
#  单线程，串行执行
def get_page(str):
    print('doing...', str)
    time.sleep(1)
    print('done', str)

name_li = ['xx', 'ww', 'ee']

start_time = time.time()
for i in name_li:
    get_page(i)
print(time.time() - start_time)

# 使用线程池方式执行
from multiprocessing.dummy import Pool

pool = Pool(2)  # todo：看一下Pool的细节,最终的执行时间不是单纯的单线程串行时间/线程数，而是考虑多个线程是怎么处理这些任务的
start_time1 = time.time()
pool.map(get_page, name_li)  # 第一个参数是阻塞的操作
print(time.time() - start_time1)

pool1 = Pool(5)  # 如果线程数量比任务数量》=的时候，实际效果和=的一样
start_time2 = time.time()
pool1.map(get_page, name_li)
print(time.time() - start_time2)


# todo:如果阻塞的操作的数量，远远多于可迭代对象（可以理解为操作对象的数量）的数量的时候，线程池的效果就没那么好了






"""
xpath 和 bs4不能解析js代码，但是正则可以的

"""
import asyncio

# async def request(url):
#     print('')