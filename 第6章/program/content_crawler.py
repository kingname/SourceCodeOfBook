import requests
import pymongo
import redis
from lxml import html

connection = pymongo.MongoClient()
db = connection.Chapter6
handler = db.white

client = redis.StrictRedis()

content_list = []
while client.llen('url_queue') > 0:
    url = client.lpop('url_queue').decode()
    source = requests.get(url).content

    selector = html.fromstring(source)
    chapter_name = selector.xpath('//div[@class="h1title"]/h1/text()')[0]
    content = selector.xpath('//div[@id="htmlContent"]/p/text()')
    content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

handler.insert(content_list)