import re
import sys
import redis

client = redis.StrictRedis()
for line in sys.stdin:
    cookie = re.search('>>>(.*?)<<<', line)
    if cookie:
        print(f'拿到Cookies：{cookie.group(1)}')
        client.lpush('login_cookies', cookie.group(1))
