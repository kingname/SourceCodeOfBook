# -*- coding: utf-8 -*-
import json
import scrapy
import datetime


class MiddlewareSpider(scrapy.Spider):
    name = "middlewareSpider"
    allowed_domains = ["kingname.info"]
    start_urls = ['http://exercise.kingname.info/exercise_middleware_retry_backend/404/{}']

    def start_requests(self):
        for i in range(1, 10):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url,
                                 method='POST',
                                 body=json.dumps({"date": str(datetime.date.today())}),
                                 headers={'Content-Type': 'application/json'})

    def parse(self, response):
        print(response.body.decode())
