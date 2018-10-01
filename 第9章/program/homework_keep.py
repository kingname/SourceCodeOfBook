import requests
import json

headers = {
    'Host': 'api.gotokeep.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'x-os-version': '7.1.2',
    'x-channel': 'yingyongbao',
    'x-locale': 'zh--CN',
    'x-screen-height': '640',
    'x-is-new-device': 'false',
    'User-Agent': 'Keep+4.7.0%2FAndroid+7.1.2-8558+Xiaomi+Redmi+4X',
    'x-manufacturer': 'Xiaomi',
    'x-keep-timezone': 'Asia/Shanghai',
    'x-screen-width': '360',
    'x-os': 'Android',
    'x-device-id': '86469803711655111111111111111111086dfde7',
    'x-version-name': '4.7.0',
    'x-user-id': '59952648094afb2485a122e3',
    'x-version-code': '8558',
    'x-model': 'Redmi+4X',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1OTk1MjY0ODA5NGFmYjI0ODVhMTIyZTMiLCJ1c2VybmFtZSI6IuavlOWwlOS8iuaBqSIsImF2YXRhciI6IiIsImdlbmRlciI6Ik0iLCJkZXZpY2VJZCI6Ijg2NDY5ODAzNzExNjU1MTExMTExMTExMTExMTExMTExMDg2ZGZkZTciLCJpc3MiOiJodHRwOi8vd3d3LmdvdG9rZWVwLmNvbS8iLCJleHAiOjE1MTI3NDgzODIsImlhdCI6MTUwNDEwODM4Mn0.I_xG1LI2twDQuoPf1S_N2Ywdv-DqugGLGt5Toz-O7RU'
           }

url = 'https://api.gotokeep.com/social/v3/timeline/hot'
hot = requests.get(url, headers=headers).content.decode()
hot_dict = json.loads(hot)
datas = hot_dict['data']['entries']
for data in datas:
    print(f'用户： {data["author"]["username"]}，内容：{data["content"]}')
