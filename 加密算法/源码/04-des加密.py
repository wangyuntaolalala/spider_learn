#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   04-des加密.py    
# Author :   柏汌  

import binascii
# 加密模式 CBC，填充方式 PAD_PKCS5
# PKCS7是兼容PKCS5的，PKCS5相当于PKCS7的一个子集。
from pyDes import des, PAD_PKCS5

def des_encrypt(key, text):
    k = des(key)
    en = k.encrypt(text.encode('utf-8'), padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)

def des_decrypt(key, text):
    k = des(key)
    de = k.decrypt(binascii.a2b_hex(text), padmode=PAD_PKCS5)
    return de.decode('utf-8')

if __name__ == '__main__':
    secret_key = '12345678'   # 密钥
    text = 'i love Python'   # 加密对象
    # iv = secret_key           # 偏移量
    secret_str = des_encrypt(secret_key, text)
    print('加密字符串：', secret_str)
    clear_str = des_decrypt(secret_key, secret_str)
    print('解密字符串：', clear_str)
