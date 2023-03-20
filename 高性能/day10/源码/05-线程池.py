#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-线程池.py    
# Author :   柏汌  


from concurrent.futures import ThreadPoolExecutor


def crawl(url):
    print(url)


if __name__ == '__main__':
    base_url = 'https://jobs.51job.com/pachongkaifa/p{}/'
    with ThreadPoolExecutor(10) as f:   # 这种写法不能守护线程，是比较呆的
        for i in range(1, 15):
            f.submit(crawl, url=base_url.format(i))
