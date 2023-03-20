#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-selenium案列.py    
# Author :   柏汌  

from selenium import webdriver
import time, random
from pymongo import MongoClient
from selenium.webdriver.common.by import By

class YwShop():
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument()
        self.browser = webdriver.Chrome()

    def base(self):
        self.browser.get('https://www.yiwugo.com/')
        inp = self.browser.find_element(By.ID, 'inputkey')
        inp.send_keys('饰品')
        self.browser.find_element(By.XPATH, '//*[@id="searchform"]/div[1]/span[2]').click()


    def save_data(self):
        pass

    def spiders(self):
        self.drop_down()
        li = self.browser.find_elements(By.CLASS_NAME, 'pro_list_product_img2')
        for j in li:
            title = j.find_element(By.XPATH, './/li/a[@class="productloc"]')
            price = j.find_element(By.XPATH, './/li/span[@class="pri-left"]/em')
            # info = j.find_element(By.XPATH, '//li/span[@class="pri-right"]/span')
            addr = j.find_element(By.XPATH, './/li[@class="shshopname"]')
            item = {
                '标题': title.text,
                '价格': price.text,
                '地址': addr.text
            }
            print(item)
        self.page_nex()

    def page_nex(self):
        next = self.browser.find_element(By.XPATH, '//*[@id="newframe"]/div/div[2]/div[3]/div[1]/ul/a[6]')
        if next:
            next.click()
            self.spiders()
        else:
            self.browser.close()

    def drop_down(self):
        for i in range(1, 11):
            j = i / 10
            js = f"document.documentElement.scrollTop = document.documentElement.scrollHeight * {j}"
            self.browser.execute_script(js)
            time.sleep(random.randint(400, 800) / 1000)


if __name__ == '__main__':
    yw = YwShop()
    yw.base()
    yw.spiders()



