import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'd_c0="AECABUmzUQqPTt7Waah4-eNbKDE-ndMJmbU=|1470061508"; _za=76e3ff3b-0533-43bf-b323-54658bd219d8; _zap=fa08520e-f1ca-4f87-a421-b6b59c6cf594; _ga=GA1.2.135017213.1483973195; aliyungf_tc=AQAAAMVqMBUkrAEA660zPUq1ZRkS1BkJ; acw_tc=AQAAAIpAiy5gpgIA660zPaCio8BzRvqC; q_c1=cbe92683816948f98932e79afd8cdc4b|1498356032000|1476533291000; q_c1=cbe92683816948f98932e79afd8cdc4b|1498356032000|1476533291000; r_cap_id="YmM1MmFmNGM1MmNlNGNkMTg5MjI5NzhiYzYyY2VkNzE=|1498699312|98d42498b4ba65f9e781f6630a3c28736e65836c"; cap_id="ZGVjYjcyYTI0YTQyNDlhODllYTM2YTZiMDE4ZTgzN2I=|1498699312|c3dea0bceadbc1df3eb778e3ec6b53b1d21e09e4"; z_c0=Mi4wQUFEQWpMb2VBQUFBUUlBRlNiTlJDaGNBQUFCaEFsVk5PT043V1FBOUVkTXdlY3lZc2tfb2YwWC11ZnlxQTM0eVFR|1498699320|a361ff4798ea0ffe11182a897b5940718fd8d823; s-q=%E5%86%B7%E7%9F%A5%E8%AF%86; s-i=3; sid=i5hj46q8; __utma=51854390.1170851395.1497785466.1500334504.1500338344.23; __utmc=51854390; __utmz=51854390.1500338344.23.12.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20131006=1^3=entry_date=20131006=1; _xsrf=73fd62f055ae3b91964cd5f9ea35fb03',
    'DNT': '1',
    'Host': 'www.zhihu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
session  = requests.Session()
source = session.get('https://zhihu.com', headers=headers, verify=False).content.decode()
x = session.get('https://www.zhihu.com/inbox/3117566900', headers=headers, verify=False).content.decode()
print(x)
