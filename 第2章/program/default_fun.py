def get_input(split_char):
    input_string = input('请输入由{}分割的两个非零整数:'.format(split_char))
    a_string, b_string = input_string.split(split_char)
    return int(a_string), int(b_string)

# a, b = get_input('#')
# print('第一个数是：{}, 第二个数是：{}'.format(a, b))

# a, b = get_input() #不小心漏掉了参数就会报错


# def get_input_with_default_para(split_char=','):
#     input_string = input('请输入由{}分割的两个非零整数:'.format(split_char))
#     a_string, b_string = input_string.split(split_char)
#     return int(a_string), int(b_string)
#
# c, d = get_input_with_default_para()
# print('第一个数是：{}, 第二个数是：{}'.format(c, d))
#
# e, f = get_input_with_default_para('*')
# print('使用*号分割的第一个数是：{}, 第二个数是：{}'.format(e, f))


# def print_x_y_z(x=100, y=0, z=50):
#     print('x的值为{}, y的值为{}, z的值为{}'.format(x, y, z))
#
# print_x_y_z(1, 2, 3) #直接写上3个参数
# print_x_y_z(6) #只写一个参数的时候，函数会从左到右依次赋值，
# print_x_y_z(y=-8) #也可以指定参数的名字，将值直接赋给指定的参数
# print_x_y_z(y='哈哈', x='嘿嘿') #如果指定了参数名，那么参数顺序就可以颠倒

# def default_para_trap(para=[], value=0):
#     para.append(value)
#     return para
#
# print('第一步')
# print('函数返回值:{}'.format(default_para_trap(value=100)))
# print('第二步')
# print('函数返回值:{}'.format(default_para_trap(value=50)))


def default_para_without_trap(para=[], value=0):
    if not para:
        para = []
    para.append(value)
    return para

print('第一步')
print('函数返回值:{}'.format(default_para_without_trap(value=100)))
print('第二步')
print('函数返回值:{}'.format(default_para_without_trap(value=50)))




