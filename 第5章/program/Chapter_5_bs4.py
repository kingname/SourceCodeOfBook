from bs4 import BeautifulSoup
import requests
import re

html = requests.get('http://exercise.kingname.info/exercise_bs_1.html').content.decode()

soup = BeautifulSoup(html, 'lxml')

useful = soup.find(class_='useful')
all_content = useful.find_all('li')
for li in all_content:
    print(li['class'])

content = soup.find_all(class_=re.compile('iam'))
for each in content:
    print(each.string)


useful = soup.find(class_='useful')
all_content = useful.find_all('li')
for li in all_content:
    print(li.string)
    print(li['class'])

content = soup.find_all(text=re.compile('我需要'))
for each in content:
    print(each.string)

info_2 = soup.find(class_='test')
print(f'使用find方法，返回的对象类型为：{type(info_2)}')
print(info_2.string)