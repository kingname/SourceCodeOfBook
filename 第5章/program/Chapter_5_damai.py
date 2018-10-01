import requests
import lxml.html
import csv

url = 'https://www.damai.cn/projectlist.do'
source = requests.get(url).content

selector = lxml.html.fromstring(source)
item_list = selector.xpath('//ul[@id="performList"]/li')

item_dict_list = []
for item in item_list:
    show_name = item.xpath('div[@class="ri-infos"]/h2/a/text()')
    show_url = item.xpath('div[@class="ri-infos"]/h2/a/@href')
    show_description = item.xpath('div[@class="ri-infos"]/p[1]/text()')
    show_time = item.xpath('div[@class="ri-infos"]/p[@class="mt5"]/text()')
    show_place = item.xpath('div[@class="ri-infos"]/p[@class="mt5"]/span[@class="ml20"]/a/text()')
    show_price = item.xpath('div[@class="ri-infos"]/p/span[@class="price-sort"]/text()')

    item_dict = {'show_name': show_name[0] if show_name else '',
                 'show_url': 'https:' + show_url[0] if show_url else '',
                 'show_description': show_description[0] if show_description else '',
                 'show_time': show_time[0].strip() if show_time else '',
                 'show_place': show_place[0] if show_place else '',
                 'show_price': show_price[0] if show_price else ''}
    item_dict_list.append(item_dict)

with open('result.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['show_name',
                                           'show_url',
                                           'show_description',
                                           'show_time',
                                           'show_place',
                                           'show_price'])
    writer.writeheader()
    writer.writerows(item_dict_list)
