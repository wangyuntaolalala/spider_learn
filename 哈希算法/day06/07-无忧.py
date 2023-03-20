import requests
import time
import execjs
from urllib.parse import urlencode,urlsplit
headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^21^^, ^\\^",
    "account-id": "",
    "From-Domain": "51job_web",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "property": "^%^7B^%^22partner^%^22^%^3A^%^22^%^22^%^2C^%^22webId^%^22^%^3A2^%^2C^%^22fromdomain^%^22^%^3A^%^2251job_web^%^22^%^2C^%^22frompageUrl^%^22^%^3A^%^22https^%^3A^%^2F^%^2Fwe.51job.com^%^2F^%^22^%^2C^%^22pageUrl^%^22^%^3A^%^22https^%^3A^%^2F^%^2Fwe.51job.com^%^2Fpc^%^2Fsearch^%^3Fkeyword^%^3Dpython^%^26searchType^%^3D2^%^26sortType^%^3D0^%^26metro^%^3D^%^22^%^2C^%^22identityType^%^22^%^3A^%^22^%^22^%^2C^%^22userType^%^22^%^3A^%^22^%^22^%^2C^%^22isLogin^%^22^%^3A^%^22^%^E5^%^90^%^A6^%^22^%^2C^%^22accountid^%^22^%^3A^%^22^%^22^%^7D",
    "sec-ch-ua-mobile": "?0",
    "user-token": "",
    "uuid": "1d238f533ca2464690f56652bda956d7",
    "partner": "",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "Origin": "https://we.51job.com",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://we.51job.com/",
    "Accept-Language": "zh-CN,zh;q=0.9"
}
url = "https://cupid.51job.com/open/noauth/search-pc"
params = {
    "api_key": "51job",
    "timestamp": str(int(time.time())),
    "keyword": "python",
    "searchType": "2",
    "function": "",
    "industry": "",
    "jobArea": "000000",
    "jobArea2": "",
    "landmark": "",
    "metro": "",
    "salary": "",
    "workYear": "",
    "degree": "",
    "companyType": "",
    "companySize": "",
    "jobType": "",
    "issueDate": "",
    "sortType": "0",
    "pageNum": "3",
    "requestId": "4632e8cb41d84656f8a3f582db8fea96",
    "pageSize": "50",
    "source": "1",
    "accountId": "",
    "pageCode": "sou|sou|soulb"
}

# 构造JS需要的明文
path = url + '?' + urlencode(params)
path = urlsplit(path)
_path = path.path + '?' + path.query
sign = execjs.compile(open('03-扣算法.js',encoding='utf-8').read()).call('run',_path)
print(sign)
headers['sign'] = sign
response = requests.get(url, headers=headers, params=params)
print(response.text)
print(response)
