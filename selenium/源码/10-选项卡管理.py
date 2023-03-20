#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   10-选项卡管理.py    
# Author :   柏汌  


import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.baidu.com')
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
time.sleep(2)
browser.quit()

