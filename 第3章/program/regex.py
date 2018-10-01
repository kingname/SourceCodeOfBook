import re

# content = '我的微博密码是：1234567，QQ密码是：33445566， 银行卡密码是：888888，Github密码是：999abc999，帮我记住他们'
#
#
# password_list = re.findall('：(.*?)，', content)
# name_list = re.findall('名字是(.*?)，', content)
# print('找到内容，返回：{}'.format(password_list))
# print('找不到任何内容，返回：{}'.format(name_list))

# account_content = '微博账号是:kingname, 密码是:12345678, QQ账号是:99999, 密码是:890abcd, 银行卡账号是:000001, 密码是:654321, Github账号是:99999@qq.com, 密码是:7777love8888, 请记住他们。'
#
# account_password = re.findall('账号是:(.*?), 密码是:(.*?),', account_content)
# print('包含多个括号的情况下，返回：{}'.format(account_password))

# big_string_mutil = '''
# 我是kingname,我的微博密码是:123
# 45678,
# '''
# password_findall_no_flag = re.findall('密码是:(.*?),', big_string_mutil)
# password_findall_flag = re.findall('密码是:(.*?),', big_string_mutil, re.S)
# print('不使用re.S的时候：{}'.format(password_findall_no_flag))
# print('使用re.的时候：{}'.format(password_findall_flag))


# content = '我的微博密码是：1234567，QQ密码是：33445566， 银行卡密码是：888888，Github密码是：999abc999，帮我记住他们'
#
# password_search = re.search('密码是：(.*?)，', content)
# password_search_not_find = re.search('xxx：(.*?)，', content)
# print(password_search)
# print(password_search.group())
# print(password_search.group(0))
# print(password_search.group(1))
# print(password_search_not_find)

# account_content = '微博账号是:kingname, 密码是:12345678, QQ账号是:99999, 密码是:890abcd, 银行卡账号是:000001, 密码是:654321, Github账号是:99999@qq.com, 密码是:7777love8888, 请记住他们。'
# account_password = re.search('账号是:(.*?), 密码是:(.*?),', account_content)
# print('读取第一个括号的内容: {}'.format(account_password.group(1)))
# print('读取第二个括号的内容: {}'.format(account_password.group(2)))


# content = '我的微博密码是：1234567，QQ密码是：33445566， 银行卡密码是：888888，Github密码是：999abc999，帮我记住他们'
# without_question_mark = re.findall('密码是：(.*)，', content)
# with_question_mark = re.findall('密码是：(.*?)，', content)
# print('不使用问号的结果: {}，长度为：{}'.format(without_question_mark, len(without_question_mark)))
# print('使用问号的结果: {}，长度为：{}'.format(with_question_mark, len(with_question_mark)))


big_small_text = '''
有效用户:
姓名: 张三
姓名: 李四
姓名: 王五
无效用户:
姓名: 不知名的小虾米
姓名: 隐身的张大侠
'''
# user = re.findall('姓名: (.*?)\n', big_small_text)
# print(user)

user_big = re.findall('有效用户(.*?)无效用户', big_small_text, re.S)
print('user_big 的值为: {}'.format(user_big))

user_useful = re.findall('姓名: (.*?)\n', user_big[0])
print('真正有效的人名：{}'.format(user_useful))

# html = '''<div class="tail-info">客户端</div>
# <div class="tail-info">2017-01-01 13:45:00</div>
# '''
#
# result_1 = re.findall('tail-info">(.*?)<', html)
# result_2 = re.findall('tail-info">2017(.*?)<', html)
# result_3 = re.findall('tail-info">(2017.*?)<', html)
# print('括号里只有.*?时，得到的结果：{}'.format(result_1))
# print('2017在括号外面时，得到的结果：{}'.format(result_2))
# print('2017在括号里面时，得到的结果：{}'.format(result_3))
