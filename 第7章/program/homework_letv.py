import re
import json
import requests


class LetvSpider(object):

    COMMENT_URL = 'http://api.my.le.com/vcm/api/list?jsonp=jQuery171029717156927084076_1504105496754&' \
                  'cid=2&type=video&rows=20&page=1&sort=&source=1&listType=1&xid={xid}&pid={pid}&' \
                  'ctype=cmt%2Cimg%2Cvote'

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Cookie': 'http://api.my.le.com/vcm/api/list?jsonp=jQuery171029717156927084076_1504105496754&cid=2&type=video&rows=20&page=1&sort=&source=1&listType=1&xid=30744694&pid=10026177&ctype=cmt%2Cimg%2Cvote',
        'DNT': '1',
        'Host': 'api.my.le.com',
        'Referer': 'http://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }

    def __init__(self, url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    def get_source(self, url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        source = self.get_source(self.url, self.HEADERS)
        vid = re.search('vid: (\d+)', source).group(1)
        pid = re.search('pid: (\d+)', source).group(1)
        self.necessary_info['xid'] = vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        url = self.COMMENT_URL.format(xid=self.necessary_info['xid'],
                                      pid=self.necessary_info['pid'])
        source = self.get_source(url, self.HEADERS)
        source_json = source[source.find('{"'): -1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人： {comment["user"]["username"]}, 评论内容：{comment["content"]}')
if __name__ == '__main__':
    spider = LetvSpider('http://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1')

