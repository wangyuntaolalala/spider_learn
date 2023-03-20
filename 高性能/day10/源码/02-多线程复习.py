#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-多线程复习.py    
# Author :   柏汌  

import threading
import time

def test():
    time.sleep(2)
    print(1111)


if __name__ == '__main__':
    for i in range(10):
        # 设置子线程为守护主线程
        t1 = threading.Thread(target=test)
        # todo:为了能够让主线程回收子线程，可以把子线程设置为守护线程,即该线程不重要，主线程结束，子线程结束
        # t1.setDaemon(True)   # 设置守护主线程
        t1.start()
    # print(222)






