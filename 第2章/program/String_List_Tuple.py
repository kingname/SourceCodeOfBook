example_string = '我是字符串'
example_list = ['我', '是', '列', '表']
example_tuple = ('我', '是', '元', '组')
print('1.取第一个元素 >', example_string[0], example_list[0], example_tuple[0])
print('2.取下标为2的元素（第三个元素）>', example_string[2], example_list[2], example_tuple[2])
print('3.取最后一个元素 >', example_string[-1], example_list[-1], example_tuple[-1])
print('4.取倒数第二个元素 >', example_string[-2], example_list[-2], example_tuple[-2])
print('5.切片0:1 >', example_string[0:1], example_list[0:1], example_tuple[0:1])
print('6.切片0:2 >', example_string[0:2], example_list[0:2], example_tuple[0:2])
print('7.切片2:4 >', example_string[2:4], example_list[2:4], example_tuple[2:4])
print('8.切片从第一个元素直到下标为1的元素 >', example_string[:2], example_list[:2], example_tuple[:2])
print('9.切片从下标为1的元素直到全部 >', example_string[1:], example_list[1:], example_tuple[1:])
print('10.切片去掉最后一个元素 >', example_string[:-1], example_list[:-1], example_tuple[:-1])
print('11.切片去掉最后两个元素 >', example_string[:-2], example_list[:-2], example_tuple[:-2])
print('12.每2个字取一个 >', example_string[::2], example_list[::2], example_tuple[::2])
print('13.将字符串、列表、元组倒序输出 >', example_string[::-1], example_list[::-1], example_tuple[::-1])


# string_1 = '你好'
# string_2 = '世界'
# string_3 = string_1 + string_2
# print(string_3)
#
#
# list_1 = ['abc', 'xyz']
# list_2 = ['哈哈哈哈', '嘿嘿嘿黑']
# list_3 = list_1 + list_2
# print(list_3)
#
# existed_list = [1, 2, 3]
# existed_list[1] = '新的值'
# print(existed_list)
#
# list_4 = ['Python', '爬虫']
# print(list_4)
# list_4.append('一')
# print(list_4)
# list_4.append('酷')
# print(list_4)