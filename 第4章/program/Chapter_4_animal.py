import requests
import re
import os
from multiprocessing.dummy import Pool


start_url = 'http://www.kanunu8.com/book3/6879/'


def get_source(url):
    """
    获取网页源代码。
    :param url: 网址
    :return: 网页源代码
    """
    html = requests.get(url)
    return html.content.decode('gbk') #这个网页需要使用gbk方式解码才能让中文正常显示


def get_toc(html):
    """
    获取每一章链接，储存到一个列表中并返回。
    :param html: 目录页源代码
    :return: 每章链接
    """
    toc_url_list = []
    toc_block = re.findall('正文(.*?)</tbody>', html, re.S)[0]
    toc_url = re.findall('href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append(start_url + url)
    return toc_url_list


def get_article(html):
    """
    获取每一章的正文并返回章节名和正文。
    :param html: 正文源代码
    :return: 章节名，正文
    """
    chapter_name = re.search('size="4">(.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block


def save(chapter, article):
    """
    将每一章保存到本地。
    :param chapter: 章节名, 第X章
    :param article: 正文内容
    :return: None
    """
    os.makedirs('动物农场', exist_ok=True) #如果没有"动物农场文件夹，就创建一个，如果有，则什么都不做"
    with open(os.path.join('动物农场', chapter + '.txt'), 'w', encoding='utf-8') as f:
        f.write(article)


def query_article(url):
    """
    根据正文网址获取正文源代码，并调用get_article函数获得正文内容最后保存到本地。
    :param url: 正文网址
    :return: None
    """
    article_html = get_source(url)
    chapter_name, article_text = get_article(article_html)
    save(chapter_name, article_text)


if __name__ == '__main__':
    toc_html = get_source(start_url)
    toc_list = get_toc(toc_html)
    pool = Pool(4)
    pool.map(query_article, toc_list)