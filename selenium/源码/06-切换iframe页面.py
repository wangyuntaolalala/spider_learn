#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-切换iframe页面.py    
# Author :   柏汌  
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.douban.com/')
iframe = browser.find_element(By.XPATH, '//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(iframe)
browser.find_element(By.CLASS_NAME, 'account-tab-account').click()
browser.find_element(By.ID, 'username').send_keys('134723456347')

