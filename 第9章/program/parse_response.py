import json
def response(flow):
    resp = flow.response
    print(f'返回的头部为：{resp.headers}')
    print(f'返回的body为：{json.loads(resp.content)}')
