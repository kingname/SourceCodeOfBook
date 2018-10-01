# -*- coding: utf-8 -*-
import scrapy
import json
import datetime


class checkSpider(scrapy.Spider):
    name = "checkSpider"
    # allowed_domains = ["xx.com"]
    start_urls = ['http://exercise.kingname.info/exercise_middleware_retry_backend/param/{}']

    def start_requests(self):
        for i in range(1, 10):
            url = self.start_urls[0].format(i)
            yield scrapy.Request(url,
                                 method='POST',
                                 body=json.dumps({"date": str(datetime.date.today())}),
                                 headers={'Content-Type': 'application/json'},
                                 meta={'page': i})

    def parse(self, response):
        if '参数错误' in response.body.decode():
            raise Exception('参数错误')
