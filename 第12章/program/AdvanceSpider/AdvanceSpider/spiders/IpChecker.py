# -*- coding: utf-8 -*-
import scrapy


class IpcheckerSpider(scrapy.Spider):
    name = "IpChecker"
    # allowed_domains = ["xx.com"]
    start_urls = ['http://exercise.kingname.info/exercise_middleware_ua',
                  'http://exercise.kingname.info/exercise_middleware_ua/2',
                  'http://exercise.kingname.info/exercise_middleware_ua/3']

    def parse(self, response):
        print(response.body.decode())
