# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import json
import time
import redis
import random
import datetime
from AdvanceSpider.items import ErrorItem
from scrapy import signals
from selenium import webdriver
from scrapy.conf import settings
from scrapy.http import HtmlResponse
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from twisted.internet.error import TCPTimedOutError


class AdvancespiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        print('========exception=========')

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = random.choice(settings['PROXIES'])
        request.meta['proxy'] = proxy


class UAMiddleware(object):

    def process_request(self, request, spider):
        ua = random.choice(settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = ua


class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def process_request(self, request, spider):
        if spider.name == 'seleniumSpider':
            self.driver.get(request.url)
            time.sleep(2)
            body = self.driver.page_source

            return HtmlResponse(self.driver.current_url,
                                body=body,
                                encoding='utf-8',
                                request=request)


class LoginMiddleware(object):
    def __init__(self):
        self.client = redis.StrictRedis()

    def process_request(self, request, spider):
        if spider.name == 'loginSpider':
            cookies = json.loads(self.client.lpop('cookies').decode())
            request.cookies = cookies


class RetryOfDateMiddleware(RetryMiddleware):
    def __init__(self, settings):
        RetryMiddleware.__init__(self, settings)

    def process_exception(self, request, exception, spider):
        if spider.name == 'exceptionSpider' and isinstance(exception, TCPTimedOutError):
            self.remove_borken_proxy(request.meta['proxy'])
            return request.copy()

    def remove_borken_proxy(self, proxy):
        """
        在这里写代码，从数据库或者是Redis中，把无效的代理剔除掉
        :param proxy:
        :return:
        """
        pass

    def process_response(self, request, response, spider):
        if spider.name == 'middlewareSpider':
            return_str = response.body.decode()
            if '404.html' not in str(response.url) and '参数错误' not in return_str:
                return response

            yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
            if '404.html' in str(response.url):
                origin_url = request.meta['redirect_urls'][0]
                next_request = request.replace(url=origin_url,
                                               method='POST',
                                               body=json.dumps({'date': yesterday}),
                                               headers={'Content-Type': 'application/json'})
            else:
                next_request = request.replace(body=json.dumps({'date': yesterday}))
            return next_request
        return response


class ExceptionCheckSpider(object):

    def process_spider_exception(self, response, exception, spider):
        if spider.name == 'checkSpider':
            print(f'返回的内容是：{response.body.decode()}\n报错原因：{exception}')
            page = response.meta['page']
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            error_item = ErrorItem()
            error_item['page'] = page
            error_item['error_time'] = now_time
            yield error_item
