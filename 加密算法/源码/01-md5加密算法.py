#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   01-md5加密算法.py    
# Author :   柏汌  

import hashlib



def md5_test():
    text = '我爱Python'
    result = hashlib.md5(text.encode('utf-8')).hexdigest()
    print(result)


md5_test()
