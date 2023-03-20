
import requests,execjs
headers = {
    "authority": "api.wei-liu.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.wei-liu.com",
    "pragma": "no-cache",
    "referer": "https://www.wei-liu.com/",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^110^^, ^\\^Not",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def get_token():
    url = 'https://api.wei-liu.com/api/v1/Token/code'
    res = requests.get(url,headers=headers)
    data = res.json().get('data')
    item1 = data.get('item1')
    item2 = data.get('item2')
    return item1,item2

def login():
    i1,i2 = get_token()
    with open('04-wly.js',encoding='utf-8') as f:
        js_code = f.read()
    cell = execjs.compile(js_code)
    pwd = cell.call('get_psd',i1,i2,'123123123')
    print(pwd)
    url = "https://api.wei-liu.com/api/v1/Token"
    data = {
        "code":'',
        "grant_type": "password",
        "language": "zh-CN",
        "password":pwd,
        "userType": "1",
        "username": '13535353535'
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.text)
    print(response)

if __name__ == '__main__':
    login()

