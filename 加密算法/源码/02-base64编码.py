#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-base64编码.py    
# Author :   柏汌  


import base64



def base64_text():
    text = '柏汌老师好帅'
    result = base64.b64encode(text.encode('utf-8'))
    print(result)

base64_text()


