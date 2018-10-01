import requests
import time
import json
import re


login_url = 'https://account.guokr.com/sign_in/'
email = 'greensouth@foxmail.com'
password = 'iamtheone847'

captcha_username = 'kingname'
captcha_password = 'baiguanlab'
captcha_appid = 1
captcha_appkey = '22cc5376925e9387a23cf797cb9ba745'
captcha_codetype = '1004'
captcha_url = 'http://api.yundama.com/api.php?method=upload'
captcha_result_url = 'http://api.yundama.com/api.php?cid={}&method=result'
guokr_captcha_url = 'https://account.guokr.com/captcha/{}'

data_guokr = {
    'username': email,
    'password': password,
    'permanent': 'y'
}
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}


def get_captcha_by_cid(cid, timeout=15):
    while timeout > 0:
        response = requests.get(captcha_result_url.format(cid)).text
        response_dict = json.loads(response)
        print(response_dict, '——还剩:{}秒...'.format(timeout))
        captcha = response_dict['text']
        if response_dict['text']:
            return captcha
        time.sleep(1)
        timeout -= 1
    return ''


def query_captcha(filename):
    data = {'method': 'upload', 'username': captcha_username, 'password': captcha_password, 'appid': captcha_appid,
            'appkey': captcha_appkey, 'codetype': captcha_codetype, 'timeout': '60'}
    f = open(filename, 'rb')
    file = {'file': f}
    response = requests.post(captcha_url, data, files=file).text
    f.close()
    response_dict = json.loads(response)
    if 'cid' not in response_dict:
        print('请在官网上查询此错误码: {}'.format(response_dict['ret']))
        exit()
    captcha = response_dict['text']
    if not captcha:
        cid = response_dict['cid']
        captcha = get_captcha_by_cid(cid)

    return captcha


session = requests.Session()

#直接访问登录页面,先获取必要信息:csrf_token, captcha_rand 和captcha地址
html = session.get(login_url, headers=header).content.decode()

csrf_token = re.findall('name="csrf_token" type="hidden" value="(.*?)">', html, re.S)
if not csrf_token:
    print('不能获取csrf_token, 无法登录。')
    exit()
csrf_token = csrf_token[0]

captcha_rand = re.findall('id="captchaRand" value="(.*?)">', html, re.S)
if not captcha_rand:
    print('不能获取captcha_rand, 无法登录。')
    exit()

captcha_rand = captcha_rand[0]
with open('guokr.png', 'wb') as f:
    f.write(requests.get(guokr_captcha_url.format(captcha_rand)).content)

captcha_solution = query_captcha('guokr.png')
data_guokr['captcha'] = captcha_solution
data_guokr['captcha_rand'] = captcha_rand
data_guokr['csrf_token'] = csrf_token
result = session.post(login_url, data=data_guokr, headers=header).content

#在登录成功以后,访问其他页面只需要使用session.get即可。
profile = session.get('http://www.guokr.com/settings/profile/', headers=header).content
print(profile.decode())


