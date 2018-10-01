import os


scrapy_project_path = '/Users/kingname/book/chapter_12/DeploySpider'
os.chdir(scrapy_project_path) #切换工作区，进入爬虫工程根目录执行命令
os.system('scrapyd-deploy')


import json
import time
import requests
start_url = 'http://45.76.110.210:6800/schedule.json'
start_data = {'project': 'DeploySpider',
              'spider': 'Example'}

end_url = 'http://45.76.110.210:6800/cancel.json'
end_data = {'project': 'DeploySpider'}

result = requests.post(start_url, data=start_data, auth=('kingname', 'genius')).text
result = requests.post(end_url, data=end_data, auth=('kingname', 'genius')).text

# result_dict = json.loads(result)
# job_id = result_dict['jobid']
# print(f'启动的爬虫，jobid为：{job_id}')
#
# time.sleep(5)
# end_data['job'] = job_id
# result = requests.post(end_url, data=end_data).text
# print(result)
