#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-基本使用.py    
# Author :   柏汌  

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 打开指定的浏览器
browser = webdriver.Chrome()
# 打开指定的页面
browser.get('https://ygp.gdzwfw.gov.cn/#/44/jygg')
# 选择输入框   输入数据
# 方法已经弃用  之前用的selenium版本是4版本之前  现在是4版本之后
# browser.find_element_by_id('kw').send_keys('python')
# 新版本的使用
# browser.find_element(By.NAME, 'wd').send_keys('selenium')
# # 通过id进行点击
# browser.find_element(By.ID, 'su').click()
# 提取页面的功能
time.sleep(4)
print(browser.page_source)
# 获取截屏
browser.get_screenshot_as_file('123.jpg')
print(browser.current_url)
browser.quit()

