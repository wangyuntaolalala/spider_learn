#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   08-动作移动.py    
# Author :   柏汌
import time

from selenium import webdriver
import random
browser = webdriver.Chrome()
browser.get('https://36kr.com/')

for i in range(1, 9):
    time.sleep(random.randint(100, 300) / 1000)
    browser.execute_script('window.scrollTo(0, {})'.format(i * 500))

