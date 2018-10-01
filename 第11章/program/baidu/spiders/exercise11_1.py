# -*- coding: utf-8 -*-
import scrapy


class Exercise111Spider(scrapy.Spider):
    name = "exercise11_1"
    allowed_domains = ["exercise.kingname.info"]
    start_urls = ['http://exercise.kingname.info/exercise_xpath_1.html']

    def parse(self, response):
        name_list = response.xpath('//li[@class="name"]/text()').extract()
        price_list = response.xpath('//li[@class="price"]/text()').extract()
        for i in range(len(name_list)):
            print('商品：{}, 价格为：{}'.format(name_list[i], price_list[i]))
