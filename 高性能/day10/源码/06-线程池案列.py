#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-线程池案列.py    
# Author :   柏汌  


import time

import requests
import pymysql
from concurrent.futures import ThreadPoolExecutor

class Baidu(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="root", db="spiders")
        self.cursor = self.db.cursor()
        self.url = 'https://talent.baidu.com/httservice/getPostListNew'
        self.headers = {
            'Referer': 'https://talent.baidu.com/jobs/social-list?search=python',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }

    def get_data(self, page):  # 获取地址和User-Agent
        data = {
            'recruitType': 'SOCIAL',
            'pageSize': 10,
            'keyWord': '',
            'curPage': page,
            'projectType': '',
        }
        response = requests.post(url=self.url, headers=self.headers, data=data)
        return response.json()

    def parse_data(self, response):
        # print(response)
        data_list = response["data"]['list']
        for node in data_list:
            education = node['education'] if node['education'] else '空'

            name = node['name']
            serviceCondition = node['serviceCondition']
            self.save_data(education, name, serviceCondition)

    def create_table(self):
        # 使用预处理语句创建表
        sql = '''
                    CREATE TABLE IF NOT EXISTS baidu(
                        id int primary key auto_increment not null,
                        education VARCHAR(255) NOT NULL, 
                        name VARCHAR(255) NOT NULL, 
                        serviceCondition TEXT)
                    '''
        try:
            self.cursor.execute(sql)
            print("CREATE TABLE SUCCESS.")
        except Exception as ex:
            print(f"CREATE TABLE FAILED,CASE:{ex}")


    def save_data(self,education, name, serviceCondition):
        # SQL 插入语句
        sql = 'INSERT INTO baidu(id, education, name, serviceCondition) values(%s, %s, %s, %s)'
        # 执行 SQL 语句
        try:
            self.cursor.execute(sql, (0, education, name, serviceCondition))
            # 提交到数据库执行
            self.db.commit()
            print('数据插入成功...')
        except Exception as e:
            print(f'数据插入失败: {e}')
            # 如果发生错误就回滚
            self.db.rollback()

    def run(self):
        self.create_table()
        with ThreadPoolExecutor(max_workers=5)as pool:
            for i in range(1, 6):
                response = pool.submit(self.get_data, i)
                self.parse_data(response.result())

        # 关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    t1 = time.time()
    baidu = Baidu()
    baidu.run()
    print("总耗时:", time.time() - t1)

