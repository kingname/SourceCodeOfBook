# -*- coding: utf-8 -*-
import scrapy


class ExceptionSpider(scrapy.Spider):
    name = "exceptionSpider"
    # allowed_domains = ["xx.com"]
    start_urls = ['http://exercise.kingname.info/exercise_middleware_ip',
                  'http://exercise.kingname.info/exercise_middleware_ip/2',
                  'http://exercise.kingname.info/exercise_middleware_ip/3']

    def parse(self, response):
        print(response.body.decode())
