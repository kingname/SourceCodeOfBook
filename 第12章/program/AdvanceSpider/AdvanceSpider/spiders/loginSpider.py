# -*- coding: utf-8 -*-
import scrapy


class LoginspiderSpider(scrapy.Spider):
    name = "loginSpider"
    allowed_domains = ["kingname.info"]
    start_urls = ['http://exercise.kingname.info/exercise_login_success']

    def parse(self, response):
        print(response.body.decode())
