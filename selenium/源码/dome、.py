import requests
import time
print(time.time())

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://ygp.gdzwfw.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://ygp.gdzwfw.gov.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "X-Dgi-Req-App": "ggzy-portal",
    "X-Dgi-Req-Nonce": "1cfZZUn5ERqJxqEP",  # 不知道是什么   加密的
    "X-Dgi-Req-Signature": "62f2d5c49a5da5e9bf41a82d33c875af286704c1a6a025f13af78b485fc97fac",  # 加密
    "X-Dgi-Req-Timestamp": "1675080275256",

}
cookies = {
    "_horizon_uid": "df156b90-0791-40a9-884c-0afecb3fdafd",
    "_horizon_sid": "848a4fdd-0099-4958-906e-65c576a1a15c"
}
url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v1/items"
false = False
data = {"type":"trading-type","publishStartTime":"","publishEndTime":"","siteCode":"44","secondType":"A","projectType":"","thirdType":"","dateType":"","total":187361,"pageNo":2,"pageSize":10,"openConvert":false}
response = requests.post(url, headers=headers, cookies=cookies, json=data)

print(response.text)
print(response)