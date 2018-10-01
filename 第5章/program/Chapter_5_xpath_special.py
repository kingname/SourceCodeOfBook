import lxml.html


html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1-k">需要的内容1</div>
    <div id="test-2-k">需要的内容2</div>
    <div id="testfault-k">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
</body>
</html>
'''

# selector = lxml.html.fromstring(html1)
# content = selector.xpath('//div[ends-with(@id, "-k")]/text()')
# for each in content:
#     print(each)

html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="abc-key-x">需要的内容1</div>
    <div id="123-key-000">需要的内容2</div>
    <div id="haha-key">需要的内容3</div>
    <div id="useless">这是我不需要的内容</div>
</body>
</html>
'''

# selector = lxml.html.fromstring(html2)
# content = selector.xpath('//div[contains(@id, "-key")]/text()')
# for each in content:
#     print(each)


html3 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''
#如果使用一般的办法，就会出现获取到的数据不完整的情况
selector = lxml.html.fromstring(html3)
# content_1 = selector.xpath('//div[@id="test3"]/text()')
# for each in content_1:
#     print(each)

# 使用string(.)就可以把数据获取完整
data = selector.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
print(info)
