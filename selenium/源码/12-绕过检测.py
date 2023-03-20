#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   12-绕过检测.py    
# Author :   柏汌  

from selenium import webdriver

# 设置屏蔽
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
browser = webdriver.Chrome(options=options)
# 无处理
browser.get('https://bot.sannysoft.com/')

