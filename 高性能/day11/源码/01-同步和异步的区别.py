#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-同步和异步的区别.py
# Author :   柏汌  


# import requests
# import time
#
# def main():
#     for i in range(30):
#         res = requests.get('https://www.baidu.com')
#         print('第{}次请求', res.status_code)
#
# if __name__ == '__main__':
#     t1 = time.time()
#     main()
#     print('总耗时是{}'.format(time.time() - t1))

import asyncio   # 想用aiohttp的话得先导入这个
import time
import aiohttp

async def requ_data(client, i):
    res = await client.get('https://www.baidu.com')   # 注意这里的await,凡是需要异步执行的，都加一下await
    print('当前执行的是{}请求，状态码是={}'.format(i, res.status))

async def main():
    # 上下文方式启动  能帮助我们自动的分配和释放资源
    # aiohttp.ClientSession() 类似于 requests的session()
    async with aiohttp.ClientSession() as client:
        tasks = []
        for i in range(30):
            # 获取到协程对象
            res = requ_data(client, i)
            # 创建成task对象
            task = asyncio.create_task(res)
            tasks.append(task)

        await asyncio.wait(tasks)
if __name__ == '__main__':
    t1 = time.time()
    # 创建事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # asyncio.run(main())

    print('总耗时是{}'.format(time.time() - t1))







