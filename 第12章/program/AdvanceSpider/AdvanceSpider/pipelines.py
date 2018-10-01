# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from AdvanceSpider.items import ErrorItem


class AdvancespiderPipeline(object):
    def __init__(self):
        self.db = pymongo.MongoClient()[settings['MONGODB_DB']]
        self.handler = None

    def process_item(self, item, spider):
        if isinstance(item, ErrorItem):
            self.process_error(item)
        return item

    def process_error(self, item):
        if not self.handler:
            self.handler = self.db[settings['MONGODB_ERROR']]
        self.handler.insert_one(dict(item))
