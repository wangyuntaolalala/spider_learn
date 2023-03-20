#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   03-SHA加密.py    
# Author :   柏汌  

import hashlib

def SHA_test():
    text = '我爱Python'
    result = hashlib.sha512(text.encode('utf-8')).hexdigest()
    print(result)
    print(len(result))

SHA_test()
