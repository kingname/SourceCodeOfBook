"""
CaptchaKiller.py
~~~~~~~~~~~~~~~~
This module is used to query captcha by Yundama which is an anti-captcha website.
The work flow is:

upload captcha-img to the website by its api and then query the result.
"""
import requests
import json
import time


class CaptchaKiller(object):
    captcha_username = 'kingname'
    captcha_password = 'baiguanlab'
    captcha_appid = 1
    captcha_appkey = '22cc5376925e9387a23cf797cb9ba745'
    captcha_codetype = '1004'
    captcha_url = 'http://api.yundama.com/api.php?method=upload'
    captcha_result_url = 'http://api.yundama.com/api.php?cid={}&method=result'

    def __init__(self):
        pass

    def get_captcha_by_cid(self, cid, timeout=15):
        while timeout > 0:
            response = requests.get(self.captcha_result_url.format(cid)).text
            response_dict = json.loads(response)
            print(response_dict, '——还剩:{}秒...'.format(timeout))
            captcha = response_dict['text']
            if response_dict['text']:
                return captcha
            time.sleep(1)
            timeout -= 1
        return ''

    def query_captcha(self, filename):
        data = {'method': 'upload',
                'username': self.captcha_username,
                'password': self.captcha_password,
                'appid': self.captcha_appid,
                'appkey': self.captcha_appkey,
                'codetype': self.captcha_codetype,
                'timeout': '60'}

        f = open(filename, 'rb')
        file = {'file': f}
        response = requests.post(self.captcha_url, data, files=file).text
        f.close()
        response_dict = json.loads(response)
        if 'cid' not in response_dict:
            print('请在官网上查询此错误码: {}'.format(response_dict['ret']))
            exit()
        captcha = response_dict['text']
        if not captcha:
            cid = response_dict['cid']
            captcha = self.get_captcha_by_cid(cid)

        return captcha

if __name__ == '__main__':
    captcha_killer = CaptchaKiller()
    captcha = captcha_killer.query_captcha('captcha.png')
    print(captcha)

