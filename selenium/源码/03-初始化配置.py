#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-初始化配置.py    
# Author :   柏汌  


from selenium import webdriver
import time
options = webdriver.ChromeOptions()

# 禁止加载图片
# prefs = {"profile.managed_default_content_settings.images": 2}
# options.add_experimental_option("prefs", prefs)

# 无头模式   在后台运行
# options.add_argument('-headless')

# 关闭受到控制
options.add_experimental_option('useAutomationExtension', False) # 去掉开发者警告
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 设置use-agent
user = '12323894578934ajshdfghj'
options.add_argument('user-agent=%s' % user)

# 不自动关闭
options.add_experimental_option('detach', True)

# 使用浏览器插件
# path = r'E:\BaiduNetdiskDownload\Chrome插件\iguge_2011\igg_2.0.11.crx'
# options.add_extension(path)

# 设置代理
# options.add_argument('--proxy-server=http://58.20.184.187:9091')



browser = webdriver.Chrome(options=options)
browser.get('https://www.baidu.com')

# 将浏览器最大化
# browser.maximize_window()
# 自己设置
browser.set_window_size(520, 520)

# 打开新的窗口   通过js代码打开
browser.execute_script('window.open("https://www.baidu.com")')


time.sleep(3)
browser.close()


