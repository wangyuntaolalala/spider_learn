#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/10/31 19:16
# @Author : Wangyt

import requests
"""
section1
1.反爬机制：验证码，识别验证码中的数据，用于模拟登陆
2.识别方式：第三方工具自动识别

"""

"""
section2
发送请求无cookie拿到的内容不一样，响应码还是200
对于很多需要登录的网页，由于http/https本身的无状态特点，引入cookie记录状态
之前遇到的，都是抓包获取的cookie,封装到headers中去，但是cookie很多都有时效性，这种处理方式的通用性不强
【问】如何自动处理cookie?   （cookie和session的关系？？？）
模拟登录post后，服务器会创建cookie,拿到这个就好了
    -session会话对象
        -请求发送
        -如果请求过程中产生了cookie,该cookie会被自动存储或者携带
    -创建一个session对象，
    -用session对象模拟登录，发送post请求
    -cookie被携带到session对象中，再用该对象发get请求

"""
# 后续的编码和post、get差不多的
session = requests.Session()


"""
section3
代理：和封ip对应
用了代理之后本地的ip不会被封，替身会被封
代理相关的网站，快代理，狸猫，

代理ip类型：用的时候，对应要请求的url的类型
    -http:
    -https:
req = requests.get(url=url,headers=headers,proxies={'http':'xx.xx.xx.xxx'})
传入字典到proxies中去即可

代理ip的匿名度：
-透明：服务器知道用了代理，知道真实ip
-匿名：知道用了代理，不知道真实的ip
-高匿：啥也不知道
"""







