#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   09-延时等待.py    
# Author :   柏汌  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
wait = WebDriverWait(browser, 10)
inp = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
but = wait.until(EC.element_to_be_clickable((By.ID, 'su')))
print(inp, but)




