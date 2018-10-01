import requests
import json
import time


url = 'http://exercise.kingname.info/ajax_5_backend'

html_json = requests.post(url,
                          headers={'ReqTime': str(int(time.time() * 1000))},
                          json={'sum': '6'}).content.decode()
html_dict = json.loads(html_json)

print(html_dict)
