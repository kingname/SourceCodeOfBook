def get_input():
    input_string = input('请输入由逗号分割的两个非零整数:')
    a_string, b_string = input_string.split(',')
    return int(a_string), int(b_string)


def calc(a, b):
    sum_a_b = a + b
    difference_a_b = a - b
    product_a_b = a * b
    quotient = a / b
    return {'sum': sum_a_b, 'diff': difference_a_b, 'pro': product_a_b, 'quo': quotient}


def output(result):
    print('两个数的和为: {}'.format(result['sum']))
    print('两个数的差为: {}'.format(result['diff']))
    print('两个数的积为: {}'.format(result['pro']))
    print('两个数的商为: {}'.format(result['quo']))


def run():
    a, b = get_input()
    result = calc(a, b)
    output(result)

run()

# a_int, b_int = get_input()
# result_dict = calc(a_int, b_int)
# output(result_dict)
