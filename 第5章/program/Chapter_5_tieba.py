import requests
import lxml.html
source = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&red_tag=g2896306195').content
selector = lxml.html.fromstring(source)
post_title_list = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
for post_title in post_title_list:
    print(post_title)
