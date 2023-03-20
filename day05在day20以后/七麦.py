
import requests
import execjs
from pprint import pprint

headers = {
    "authority": "api.qimai.cn",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^21^^, ^\\^",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "origin": "https://www.qimai.cn",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.qimai.cn/",
    "accept-language": "zh-CN,zh;q=0.9"
}
cookies = {
    "Hm_lvt_ff3eefaf44c797b33945945d0de0e370": "1677240749",
    "PHPSESSID": "idkb3tsh9ov7n7joqlibpk2vc3",
    "qm_check": "A1sdRUIQChtxen8tJ0NMNi8zcX5zHBl+YnElKyJEPxw8WkVRVRliYGBBUVNSSFk2VEdGX0kQc2g0QicNChwZQQR2AQgQQks+VzxUWAkJagJtABUQcAslU1JJS0lUBRkDBRcBBgBYS0FIWhoSUFRZEgMSBBRRTlNISFVKF0o^%^3D",
    "gr_user_id": "9b39cb33-bb94-4a39-bd26-e7447d47d524",
    "ada35577182650f1_gr_session_id": "16b788ed-a561-414f-a3df-53b594555364",
    "ada35577182650f1_gr_session_id_16b788ed-a561-414f-a3df-53b594555364": "true",
    "syncd": "-167466",
    "Hm_lpvt_ff3eefaf44c797b33945945d0de0e370": "1677245512",
    "synct": "1677245741.400",
    "tgw_l7_route": "1ed618a657fde25bb053596f222bc44a"
}
url = "https://api.qimai.cn/rank/index"
cell = execjs.compile(open('七麦.js',encoding='utf-8').read())
parmas = {
    "brand": "free",
    "device": "iphone",
    "country": "cn",
    "genre": "36",
    "date": "2023-02-24",
    "page": "1",
    "is_rank_index": "1"
}
keu = list(parmas.values())
print(keu)
analysis = cell.call('_xl',keu,'/rank/index')
parmas['analysis'] = analysis
response = requests.get(url, headers=headers, cookies=cookies, params=parmas)
pprint(response.json().get('rankInfo'))
# 50 条数据 1页


'''
 接单方向
 行业
 
'''