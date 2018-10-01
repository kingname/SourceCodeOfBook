# -*- coding: utf-8 -*-
import scrapy
from baidu.items import PersonInfoItem

class Exercise113Spider(scrapy.Spider):
    name = "exercise11_3"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ['http://exercise.kingname.info/exercise_xpath_3.html']

    def parse(self, response):
        person_list = response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfoItem()
            person_info = person.xpath('td/text()').extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item
