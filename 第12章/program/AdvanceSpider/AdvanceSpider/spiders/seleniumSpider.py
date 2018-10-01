# -*- coding: utf-8 -*-
import scrapy


class SeleniumspiderSpider(scrapy.Spider):
    name = "seleniumSpider"
    # allowed_domains = ["xxx.com"]
    start_urls = ['http://exercise.kingname.info/exercise_ajax_1.html']

    def parse(self, response):
        content_get = response.xpath('//div[@class="content_get"]/text()').extract()[0]
        content_post = response.xpath('//div[@class="content_post"]/text()').extract()[0]
        print('content_get: {content_get}'.format(content_get=content_get))
        print('content_post: {content_post}'.format(content_post=content_post))
