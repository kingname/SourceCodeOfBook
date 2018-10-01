import re
import csv

with open('source.txt', 'r', encoding='UTF-8') as f:
    source = f.read()


result_list = []

# 结果是正确的，但是逻辑上有点问题
# username_list = re.findall('username="(.*?)"', source, re.S)
# content_list = re.findall('j_d_post_content ">(.*?)<', source, re.S)
# reply_time_list = re.findall('class="tail-info">(2017.*?)<', source, re.S)
#
# for i in range(len(username_list)):
#     result = {'username': username_list[i],
#               'content': content_list[i],
#               'reply_time': reply_time_list[i]}
#     result_list.append(result)

# 逻辑上更合理的代码
# 首先获得包含每一层楼所有信息的大文本块
every_reply = re.findall('l_post l_post_bright j_l_post clearfix  "(.*?)p_props_tail props_appraise_wrap', source, re.S)

# 从每一个大文本块里面提取出各个楼层的发帖人姓名,发帖内容和发帖时间
for each in every_reply:
    result = {}
    result['username'] = re.findall('username="(.*?)"', each, re.S)[0]
    result['content'] = re.findall('j_d_post_content ">(.*?)<', each, re.S)[0].replace('            ', '')
    result['reply_time'] = re.findall('class="tail-info">(2017.*?)<', each, re.S)[0]
    result_list.append(result)

with open('tieba.csv', 'w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'content', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
