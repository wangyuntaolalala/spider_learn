#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-异步图书数据下载.py    
# Author :   柏汌  


import random
import time

import aiohttp
import asyncio
import aiomysql

# 1小时47分钟处
class Book_spider():
    def __init__(self):
        self.url = 'https://spa5.scrape.center/api/book/?limit=18&offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    async def get_Data(self, page, client, conn, cursor):
        response = await client.get(self.url.format(page * 18), headers=self.headers)
        json_data = await response.json()
        for data in json_data['results']:
            item = {}
            item['authors'] = ','.join(''.join(x.strip() for x in i.strip().split('\n')) for i in data['authors'])
            item['name'] = data['name']
            item['score'] = data['score']
            await self.save_data(item, conn, cursor)

    async def save_data(self, item, conn, cursor):
        sql_in = 'INSERT INTO books(id, authors, title, score) values(%s, %s, %s, %s)'
        try:
            await cursor.execute(sql_in, (0, item['authors'], item['name'], item['score']))
            await conn.commit()
            # await asyncio.sleep(random.randint(800, 1200) / 1000)
            print('插入数据成功')
        except Exception as e:
            print(e)
            # await conn.rollback()


    async def main(self):
        # 创建了一个异步连接池
        pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, user='root', password='root', db='spiders9',
                                          minsize=1, maxsize=1, loop=loop)
        # 链接mysql
        async  with pool.acquire() as conn:
            async with conn.cursor() as cursor:

        # conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders9',
        #                               loop=loop)
        # cursor = await conn.cursor()
        # 创建表的语法
                sql = """
                CREATE TABLE IF NOT EXISTS books(
                                id int primary key auto_increment not null,
                                authors VARCHAR(255) NOT NULL, 
                                title VARCHAR(255) NOT NULL, 
                                score VARCHAR(255) NOT NULL
                                );
                
                
                """
                await cursor.execute(sql)
                async with aiohttp.ClientSession(headers=self.headers)as client:
                    tasks = []
                    for i in range(30):
                        res = self.get_Data(i, client, conn, cursor)
                        task = asyncio.create_task(res)
                        tasks.append(task)
                    await asyncio.sleep(random.randint(500, 800) / 1000)
                    await asyncio.wait(tasks)

        # await cursor.close()
        # conn.close()
if __name__ == '__main__':
    t1 = time.time()
    book = Book_spider()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(book.main())
    print('总耗时{}'.format(time.time() - t1))