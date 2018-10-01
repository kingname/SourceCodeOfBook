import requests
import json

url = 'http://exercise.kingname.info/exercise_headers_backend'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'anhao': 'kingname',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'DNT': '1',
    'Host': 'exercise.kingname.info',
    'Referer': 'http://exercise.kingname.info/exercise_headers.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

html_json = requests.get(url, headers=headers).content.decode()
html_dict = json.loads(html_json)

print(html_dict)

