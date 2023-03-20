#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @File  :   02-豆果美食.py    
# Author :   柏汌
import json

import requests


def get_data(page):
    url = "https://api.douguo.net/home/notes/{}/20".format(page * 20)
    headers = {
        'uuid': '3a1168d0-87ec-48a9-b18d-483217a2e9c6',
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; SM-G973N Build/PPR1.190810.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36'
    }
    data = {
        'client':'4',
        '_session':'1675257901230351564608872123',
        'direction':'2',
        'btmid':'[31471780,29525891]',
        'is_new_user':'0',
        'request_count':'19',
        'sign_ran':'70a98b0c56472735b5dafd09df1c8abb',
        'code':'cb03bb13b20fa2db',

    }
    response = requests.post(url, headers=headers, data=data)
    # print(response.json())
    return response.json()

def save_data(item):
    with open('douguo.json', 'a+', encoding='utf-8')as f:
        f.write(json.dumps(item, indent=2, ensure_ascii=False))
        f.write(',\n')

def paras_data(res):
    for i in res['result']['list']:
        item = {}
        item['title'] = i['note']['title']
        item['name'] = i['note']['author']['n']
        save_data(item)



def main():
    for i in range(3):
        res = get_data(i)
        paras_data(res)

if __name__ == '__main__':
    main()