# def response(flow):
#     req = flow.request
#     response = flow.response
#     if 'kingname.info' in req.url:
#         print('这是kingname的网站，也是我的目标网站')
#         print(f'请求的headers是： {req.headers}')
#         print(f'请求的UA是： {req.headers["User-Agent"]}')
#         print(f'返回的内容是：{response.text}')


def response(flow):
    req = flow.request
    if 'kingname.info' in req.url:
        cookies = req.headers.get('Cookie', '')
        if cookies:
            print(f'>>>{cookies}<<<')
