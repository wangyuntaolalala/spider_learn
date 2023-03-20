#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-多线案列.py    
# Author :   柏汌  

from queue import Queue
import threading
import requests
import time
import pymongo


# 高内聚 低耦合

class Aiqiyi():
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.collection = self.client['spiders9']['aqy1']
        self.url = 'https://pcw-api.iqiyi.com/search/recommend/list?channel_id=2&data_type=1&mode=24&page_id={}&ret_num=48&session=f6ad9870112eb98638f2c66c1d36e96c&three_category_id=15;must'
        self.headers = {
            'referer': 'https://list.iqiyi.com/www/2/15-------------24-1-1-iqiyi--.html?s_source=PCW_SC',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        self.url_queue = Queue()
        self.json_queue = Queue()
        self.con_list_queue = Queue()

    def get_url(self):
        time.sleep(2)  # 加这句是故意让队列里面没有内容，最终执行join计数为0 ，程序结束
        for i in range(1, 5):
            self.url_queue.put(self.url.format(i))

    def get_data(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers).json()
            # print(response.json())
            self.json_queue.put(response)
            self.url_queue.task_done()  # 加task_done的作用是让队列的计数-1，用于与最终的主线程阻塞处join连用

    def parse_data(self):
        while True:
            data = self.json_queue.get()
            video_data = data['data']['list']
            for video in video_data:
                item = {}
                item['title'] = video['title']
                item['playUrl'] = video['playUrl']
                item['description'] = video['description']
                self.con_list_queue.put(item)
            self.json_queue.task_done()

    def save_data(self):
        while True:
            item = self.con_list_queue.get()
            print(item)
            self.collection.insert_one(item)
            self.con_list_queue.task_done()

    def main(self):
        thread_list = []
        # 开启获取地址任务  获取url地址
        t_url = threading.Thread(target=self.get_url)
        thread_list.append(t_url)
        # 发送请求
        for i in range(4):  # 这里相当于4个人干一件事儿
            t_get = threading.Thread(target=self.get_data)
            thread_list.append(t_get)
        # 提取数据
        for i in range(6):
            t_par = threading.Thread(target=self.parse_data)
            thread_list.append(t_par)
        t_save = threading.Thread(target=self.save_data)
        thread_list.append(t_save)
        # todo: 积累
        for t in thread_list:
            # 因为子线程中存在死循环，所以不能让主线程等待，等待的话程序执行不完了
            t.setDaemon(True)  # 守护主线程  子线程不重要
            t.start()
        time.sleep(3)
        # 不写这块儿的话，子线程还没有执行，主线程就结束了，所以还得引入阻塞主线程的机制
        # 这里有一个坑，如果程序执行到这里时url队列中还没有url，则url队列和后续的这些队列都是空的，join的计数也是空的，0，程序会直接跳过这里的，最好在这行的前面加一个等待时间，让队列里面有内容
        for q in [self.url_queue, self.json_queue, self.con_list_queue]:
            q.join()  # 让主线程阻塞   直到计数为0


if __name__ == '__main__':
    t1 = time.time()
    aqy = Aiqiyi()
    aqy.main()
    print('总用时：', time.time() - t1)
