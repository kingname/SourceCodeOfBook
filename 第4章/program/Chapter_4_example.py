import requests
import re

html = requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
title = re.search('title>(.*?)<', html, re.S).group(1)
content_list = re.findall('<p>(.*?)<', html, re.S)
content_str = '\n'.join(content_list)
print(f'页面标题为：{title}')
print(f'页面正文内容为：\n{content_str}')



# data = {'name': 'kingname', 'password': '1234567'}
# # html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', data=data)
# html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', json=data)
# print(html_formdata.content.decode())



