#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   06-推导式.py    
# Author :   柏汌  

a = ['\n                [美]\n            艾萨克·阿西莫夫', '读客文化', '银河帝国']
print(','.join(''.join(x.strip() for x in i.strip().split('\n')) for i in a))




