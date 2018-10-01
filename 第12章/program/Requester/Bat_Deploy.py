import requests
import os

server_list = ['45.76.110.210:6800',
               '123.55.11.89.98:6800',
               '67.10.123.96:6800',
               '77.82.32.10.6:6800'
               ]

start_url = 'http://{server}/schedule.json'
scrapy_project_folder = '/Users/kingname/book/chapter_12/DeploySpider'
scrapy_cfg_template_path = os.path.join(scrapy_project_folder, 'scrapy_template.cfg')
os.chdir(scrapy_project_folder)  # 切换工作区，进入爬虫工程根目录执行命令
project = 'DeploySpider'
spider = 'Example'

with open(scrapy_cfg_template_path, encoding='utf-8') as f:
    scrapy_cfg_template = f.read()


def deploy(server):
    scrapy_cfg = scrapy_cfg_template.replace('$server$', server)
    with open('scrapy.cfg', 'w', encoding='utf-8') as f:
        f.write(scrapy_cfg)
    os.system('scrapyd-deploy')


def launch(server):
    url = start_url.format(server=server)
    start_data = {'project': project,
                  'spider': spider}
    result = requests.post(url, data=start_data).text
    print('服务器 {server}爬虫运行结果：{result}'.format(server=server,
                                                       result=result))


if __name__ == '__main__':
    for server in server_list:
        deploy(server)
        launch(server)
