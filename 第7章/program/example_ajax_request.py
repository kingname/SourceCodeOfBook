import requests

url_post = 'http://exercise.kingname.info/ajax_1_postbackend'

html_kingname = requests.post(url_post, json={'name': '青南', 'age': 24}).content.decode()
html_other = requests.post(url_post, json={'name': '无名小卒', 'age': 4}).content.decode()

print(html_kingname)
print(html_other)



# url = 'http://exercise.kingname.info/ajax_1_backend'
#
# html = requests.get(url).content.decode()
#
# print(html)

