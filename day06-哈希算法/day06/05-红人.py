import urllib3,requests,time,json
urllib3.disable_warnings()
import hashlib

months = input("请输入查询月份：")
days = input("请输入查询日期,2天以内：")
times = str(int(time.time()) * 1000)
params = {"no":"dy0002","data":{"days":1,"rankType":5,"liveDay":f"2023-{months.zfill(2)}-{days.zfill(2)}"}}
print(params)
dd = json.dumps(params)
def get_sign():
    data = f'param={dd}&timestamp={times}&tenant=1&salt=kbn%&)@<?FGkfs8sdf4Vg1*+;`kf5ndl$'  # 要进行加密的数据
    data_sha = hashlib.sha256(data.encode('utf-8')).hexdigest()
    return data_sha

def get_data():
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "ucp.hrdjyun.com:60359",
        "Origin": "http://www.hh1024.com",
        "Pragma": "no-cache",
        "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    session = requests.session()
    s = get_sign()
    t = "这里面是登陆后的token值"
    datas = {"param":dd,"sign":s,"tenant":"1","timestamp":times,"token":t}
    url = 'https://ucp.hrdjyun.com:60359/api/dy'
    res = session.post(url,headers=headers,data=json.dumps(datas))
    if res.json().get('status') == 0:
        data = res.json().get('data')['rankList']
        for d in data:
            items = {}
            items['抖音名'] = d.get('anchorName')
            items['带货销量'] ='%.2f' % (d.get('salesVolume') / 10000) + '万'
            print(items)

if __name__ == '__main__':
    reads = """
        本接口只开放抖音带货销量日榜
        可以根据日期查询
                                --- 夏洛
        """
    print(reads)
    get_data()