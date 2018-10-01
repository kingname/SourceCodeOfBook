# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from baidu.items import BlogItem
from lxml import etree
from html import unescape


class BlogSpider(RedisSpider):
    name = "BlogSpider"
    allowed_domains = ["www.kingname.info"]
    redis_key = 'blogspider'
    start_urls = ['https://www.kingname.info/archives/']
    host = 'https://www.kingname.info'

    def parse(self, response):
        title_tag_list = response.xpath('//a[@class="post-title-link"]')
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').extract_first()
            article_url = self.host + title_tag.xpath('@href').extract_first()
            item = BlogItem()
            item['title'] = article_title
            item['url'] = article_url
            yield scrapy.Request(article_url,
                                 headers=self.settings['HEADERS'],
                                 callback=self.parse_detail,
                                 meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        post_time = response.xpath('//time[@title="Post created"]/@datetime').extract_first()
        category = response.xpath('//span[@itemprop="about"]/a/span/text()').extract_first()
        post_body = response.xpath('//div[@class="post-body"]')
        body_html = unescape(etree.tostring(post_body[0]._root).decode())
        item['post_time'] = post_time
        item['category'] = category
        item['detail'] = body_html
        yield item
