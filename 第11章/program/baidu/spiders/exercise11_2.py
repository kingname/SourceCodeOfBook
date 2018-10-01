# -*- coding: utf-8 -*-
import scrapy


class Exercise112Spider(scrapy.Spider):
    name = "exercise11_2"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ['http://exercise.kingname.info/exercise_xpath_2.html']

    def parse(self, response):
        item_list = response.xpath('//ul[@class="item"]')
        for item in item_list:
            name = item.xpath('li[@class="name"]/text()').extract()
            price = item.xpath('li[@class="price"]/text()').extract()
            name = name[0] if name else 'N/A'
            price = price[0] if price else 'N/A'
            print('商品：{}, 价格为：{}'.format(name, price))
