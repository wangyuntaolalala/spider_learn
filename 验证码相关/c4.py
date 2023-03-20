#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/11/1 19:43
# @Author : Wangyt

"""
scrapy
-啥是框架：
    功能多，通用性强，像是在做填空题
-咋学框架：
    知道功能及其详细用法知道了就好了，后续可以看源码

-功能：
高性能持久化存储
高性能数据解析
分布式
异步数据下载

"""

"""
scrapy使用
1.scrapy startproject xxx 创建工程
2.cd spider
3.scrapy genspider name url:   name:爬虫py文件(唯一标识),  url：start_urls，
    -allowed_domains 



4.scrapy crawl name  后面加上--nolog之后，日志不输出，但是报错了的话也不输出，较好的方法是在settings.py中指定LOG_LEVEL = 'ERROR'
"""
"""
class Phi_spier(scrapy.Spider):
    name = 'phi_spi'   #注意cfg文件下的对应的爬虫项目，要转到那个项目下执行才可以，不然提示没有crawl指令
    #限制start_urls中某个域名对应的内容，不对应的时候不能抓,为了避免后续获取到的内容重定向，或者资源域名和网站域名不对应，这个变量往往注释掉
    allowed_domains = ['url.jspfans.com']  
    
    start_urls = ['http://url.jspfans.com/index.jspx']   #scrapy自动向该url发送请求，
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://url.jspfans.com/index.jspx',
            formdata=data,
            callback=self.parse,
            headers=self.headers,
            cookies=self.cookies,
        )

    def parse(self, response):  response对应对start_urls发送的请求，parse会被多次调用，和start_urls对应
        it = ScraphishItem()
        it['URL'] = response.xpath('//*[@id="j_idt5:view1:j_idt36_content"]/table[2]/tbody/tr[1]/td[2]').get()
        logger.info(it['URL'])
"""


