#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-采集快代理免费ip.py    
# Author :   柏汌  

import time
import requests
from lxml import etree



class Daili():
    def __init__(self):
        self.base_url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.test_url = 'http://httpbin.org/ip'   # 这个网站可以返回当前请求的ip
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

    def get_data(self, url):
        dizhi = []
        response = requests.get(url, headers=self.headers)
        data = etree.HTML(response.text)
        for tr in data.xpath('//div[@id="list"]//tbody/tr'):
            addr = {'ip': tr.xpath('./td[1]/text()')[0], 'port': tr.xpath('./td[2]/text()')[0]}
            dizhi.append(addr)
            print(addr)
        return dizhi

    def save_data(self, data):
        ips = []
        for i in data:
            proxies = {'http': 'http://' + i['ip'] + ':' + i['port']}  # todo: 注意代理的格式
            print(proxies)
            try:
                response = requests.get(self.test_url, headers=self.headers, proxies=proxies, timeout=2)
                if response.status_code == 200:
                    print(response.text)
                    ips.append(proxies)

            except Exception:
                print('当前ip不能用')
        print(ips)

    def run(self):
        for i in range(1, int(input('请输入你需要采集的页数：'))):
            ips = self.get_data(self.base_url.format(i))
            self.save_data(ips)


if __name__ == '__main__':
    Daili().run()



