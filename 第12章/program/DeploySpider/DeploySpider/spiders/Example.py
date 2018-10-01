# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "Example"
    allowed_domains = ["kingname.info"]
    start_urls = ['http://kingname.info/']

    def start_requests(self):
        for i in range(20):
            yield scrapy.Request('http://exercise.kingname.info/exercise_middleware_ip/{}'.format(i))

    def parse(self, response):
        print(response.body.decode())

