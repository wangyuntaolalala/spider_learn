#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-多进程复习.py
# Author :   柏汌  

from multiprocessing import Process
# 进程专用队列
from multiprocessing import JoinableQueue as Queue



def test(a):
    print(a)

# 多进程其实是比较耗费资源的
if __name__ == '__main__':
    for i in range(10):
        p1 = Process(target=test, args=('3333', ))
        p1.start()








