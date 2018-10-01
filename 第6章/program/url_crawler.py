import requests
from lxml import html
import redis

client = redis.StrictRedis()
source = requests.get('http://dongyeguiwu.zuopinj.com/5525').content
selector = html.fromstring(source)

url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')
for url in url_list:
    client.lpush('url_queue', url)