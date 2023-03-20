#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   07-动作连.py    
# Author :   柏汌  

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
fi = browser.find_element(By.XPATH, '//*[@id="iframeResult"]')
browser.switch_to.frame(fi)
source = browser.find_element(By.CLASS_NAME, 'ui-draggable')
target = browser.find_element(By.CLASS_NAME, 'ui-droppable')
action = ActionChains(browser)
action.drag_and_drop(source, target)
action.perform()