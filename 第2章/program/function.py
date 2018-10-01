# def func_example_1():
#     a = 1 + 1
#     return a
#     b = 2 + 2
#     print(b)
#
#
# def func_example_2(x):
#     if x <= 0:
#         return x
#     elif 0 < x <= 1:
#         return x * 10
#     else:
#         return 100
#
# print(func_example_1())


a = [1, 2, 3]
b = 0


def change_list(para):
    para.append(4)
    para.append(5)
    para.append(6)


def change_int(para):
    para = 100

print('列表原来为：{}'.format(a))
change_list(a)
print('列表被修改为：{}'.format(a))

print('变量原来为：{}'.format(b))
change_int(b)
print('变量现在为:{}'.format(b))
