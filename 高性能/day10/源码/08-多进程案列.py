#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   08-多进程案列.py    
# Author :   柏汌  

import requests
import pymongo
import time
from multiprocessing import Process
from multiprocessing import JoinableQueue as Queue
# win下：创建进程时，相当于额外开辟一个py文件，会把类中的属性拷贝一份，会导致序列化问题，mac下不会，这个就比较底层了
# client = pymongo.MongoClient(host='127.0.0.1', port=27017)
# collection = client['spiders9']['mangguo']

class Mangguo(object):
    client = pymongo.MongoClient(host='127.0.0.1', port=27017)
    collection = client['spiders9']['mangguo']

    def __init__(self):
        self.url = 'https://pianku.api.mgtv.com/rider/list/pcweb/v3?allowedRC=1&platform=pcweb&channelId=2&pn={}&pc=80&hudong=1&_support=10000000&kind=a1&area=a1&year=all&chargeInfo=a1&sort=c2'
        self.headers = {
            'referer': 'https://www.mgtv.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        self.url_queue = Queue()
        self.json_queue = Queue()
        self.con_queue = Queue()

    def get_url(self):
        for i in range(1, 10):
            self.url_queue.put(self.url.format(i))   # todo:format方法对应的字符串中如果有本来就属于字符串的{}时怎么办

    def get_data(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, headers=self.headers).json()
            self.json_queue.put(response)
            # print(response.json())
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            response = self.json_queue.get()
            video_data = response['data']['hitDocs']
            for video in video_data:
                item = {}
                item['title'] = video['title']
                item['updateInfo'] = video['updateInfo']
                item['subtitle'] = video['subtitle']
                self.con_queue.put(item)
            self.json_queue.task_done()

    def save_data(self):
        while True:
            item = self.con_queue.get()
            print(item)
            self.collection.insert_one(item)
            self.con_queue.task_done()

    def main(self):
        process_list = []

        p_url = Process(target=self.get_url)
        process_list.append(p_url)
        # 发送请求
        for i in range(3):
            p_get = Process(target=self.get_data)
            process_list.append(p_get)

        # 提取数据
        for i in range(4):
            p_pa = Process(target=self.parse_data)
            process_list.append(p_pa)
        # 保存数据
        for i in range(3):
            p_save = Process(target=self.save_data)
            process_list.append(p_save)
        for p in process_list:
            p.daemon = True  # 把进程设置成守护主进程,和04-多线程案例对应的写法不同，但是作用一样
            p.start()

        time.sleep(5)   # 这里等待一下，不然直接错过这里了
        for q in [self.url_queue, self.json_queue, self.con_queue]:
            q.join()


if __name__ == '__main__':
    t1 = time.time()
    mg = Mangguo()
    mg.main()
    print('总耗时：', time.time() - t1)
