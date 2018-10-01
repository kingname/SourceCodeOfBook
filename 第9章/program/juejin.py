import requests
import json


url = 'https://timeline-merger-ms.juejin.im/v1/get_entry_by_timeline?before=&category=57be7c18128fe1005fa902de&limit=20&src=ios&type='

headers = {
    'Host': 'timeline-merger-ms.juejin.im',
    'Accept': '*/*',
    'Cookie': 'QINGCLOUDELB=47f7a729e0fcb7fdf0b3143c89790b65ab7e48fb3972913efd95d72fe838c4fb|W0Nyw|W0Nyw',
    'User-Agent': 'Xitu/5.3.0 (iPad; iOS 11.4; Scale/2.00)',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive'}

result = requests.get(url, headers=headers, verify=False).text
article_info = json.loads(result)
for article in article_info['d']['entrylist']:
    print(article['title'])
