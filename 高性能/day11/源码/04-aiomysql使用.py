#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-aiomysql使用.py    
# Author :   柏汌  

import aiomysql
import asyncio


loop = asyncio.get_event_loop()


async def text_mysql():
    conn = await aiomysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders9', loop=loop)
    cur = await conn.cursor()
    await cur.execute('select * from baidu')
    print(cur.fetchall())

    await cur.close()
    conn.close()

loop.run_until_complete(text_mysql())


