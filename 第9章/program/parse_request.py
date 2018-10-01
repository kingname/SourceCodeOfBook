def request(flow):
    req = flow.request
    print(f'当前请求的URL为： {req.url}')
    print(f'当前的请求方式为： {req.method}')
    print(f'当前的Cookies为： {req.cookies}')
    print(f'请求的body为: {req.text}')