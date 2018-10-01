

# example_dict = {'superman': '超人是一个可以在天上飞的两足兽。它一般喜欢把内裤穿在外面',
#           '天才': '天才跑在时代的前面，把时代拖得气喘吁吁。',
#           'xx': 0,
#                 42: '42 is the answer of everything.'}
#
# print(example_dict['天才'])
# print(example_dict.get(42))
# print(example_dict.get('不存在的key'))
# print(example_dict.get('不存在的key', '找不到'))
#
#
# existed_dict = {'a': 123, 'b': 456}
# print(existed_dict)
# existed_dict['b'] = '我修改了b'
# print(existed_dict)
# existed_dict['new'] = '我来也'
# print(existed_dict)

duplicated_list = [3, 1, 3, 2, 4, 6, 6, 7, 's', 's', 'a']
unique_list = list(set(duplicated_list))
print(unique_list)