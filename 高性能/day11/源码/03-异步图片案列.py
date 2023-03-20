#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-异步图片案列.py    
# Author :   柏汌  

import asyncio
import aiohttp
import os
import time


class Crawl_img():
    def __init__(self):
        self.url = 'https://pvp.qq.com/web201605/js/herolist.json'
        self.skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

    async def spider_img(self, session, enam, cname):
        for i in range(1, 10):   # 设置了皮肤个数的上限，其实直接拿的话得处理相关的字段
            # asyncio.sleep(1)
            response = await session.get(self.skin_url.format(enam, enam, i))
            # staus 获取状态嘛
            if response.status == 200:
                content = await response.read()
                with open('图片/' + cname + '-' + str(i) + '.jpg', 'wb')as f:
                    f.write(content)
                    print('正在下载{}第{}张'.format(cname, i))
            else:
                break

    async def run(self):
        async with aiohttp.ClientSession(headers=self.headers)as session:
            response = await session.get(self.url)
            wzry_data = await response.json(content_type=None)
            # print(wzry_data)
            tasks = []
            for i in wzry_data:
                ename = i['ename']
                cname = i['cname']
                # 创建协程对象  task对象
                res = self.spider_img(session, ename, cname)
                task = asyncio.create_task(res)
                tasks.append(task)
            await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    if not os.path.exists('图片'):
        os.mkdir('图片')

    wzry = Crawl_img()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wzry.run())
    print('程序用的时间是：', time.time() - t1)
