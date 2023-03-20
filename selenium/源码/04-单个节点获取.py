#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-单个节点获取.py    
# Author :   柏汌  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   # 模拟键盘操作

browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
# 获取的数据只有一个标签
s = browser.find_element(By.NAME, 'wd')
s.send_keys('柏汌')
s.send_keys(Keys.ENTER)  # 键盘回车



# id选择器
# text = browser.find_element(By.ID, 'kw')
# text.send_keys('aaa')


# css选择器
# s = browser.find_element(By.CSS_SELECTOR, 'input.s_ipt')
# s.send_keys('dd')

# xpath选择器
t = browser.find_element(By.XPATH, '//input[@id="kw"]')
t.send_keys('haha')


