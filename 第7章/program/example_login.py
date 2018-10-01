import requests
import json

url = 'http://exercise.kingname.info/ajax_4_backend'
code_json = requests.post(url, json={'username': 'kingname', 'password': 'genius'}).content.decode()
code_dict = json.loads(code_json)
print(code_dict['code'])
