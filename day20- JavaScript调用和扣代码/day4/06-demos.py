
import requests

url = 'http://127.0.0.1:8080/user'
params = {
    'name':'123456'
}
res = requests.get(url,params=params)
print(res.text)
