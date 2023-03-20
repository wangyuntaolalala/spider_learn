#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   05-多个节点获取.py    
# Author :   柏汌  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 模拟键盘操作
browser = webdriver.Chrome()
browser.get('https://www.icswb.com/channel-list-channel-161.html')
# 获取的数据是列表
lis = browser.find_elements(By.CSS_SELECTOR, '#NewsListContainer li')
for li in lis:
    print(li)






