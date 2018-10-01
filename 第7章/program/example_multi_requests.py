import json
import re
import requests

url = 'http://exercise.kingname.info/exercise_ajax_3.html'
first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
second_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'

page_html = requests.get(url).content.decode()
secret_2 = re.search("secret_2 = '(.*?)'", page_html, re.S).group(1)

ajax_1_json = requests.get(first_ajax_url).content.decode()
ajax_1_dict = json.loads(ajax_1_json)
secret_1 = ajax_1_dict['code']

ajax_2_json = requests.post(second_ajax_url, json={'name': '青南',
                                                   'age': 24,
                                                   'secret1': secret_1,
                                                   'secret2': secret_2}).content.decode()
ajax_2_dict = json.loads(ajax_2_json)
code = ajax_2_dict['code']
print(f'最终页面显示的内容：{code}')

# url = 'http://exercise.kingname.info/ajax_3_postbackend'
# return_json_1 = requests.post(url, json={"name": "xx",
#                                          "age": 24,
#                                          "secret1": "123",
#                                          "secret2": "456"})
#
# return_json_2 = requests.post(url, json={"name": "xx",
#                                          "age": 24})
# print(f'乱写secret1和secret2, 返回：{json.loads(return_json_1.content.decode())}')
# print(f'不写secret1和secret2，返回：{json.loads(return_json_2.content.decode())}')


# html_json = '{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u54ce\u54df\u4e0d\u9519\u54e6", "success": true}'
# html_dict = json.loads(html_json)
#
# print(html_dict)