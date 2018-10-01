import lxml.html

source = '''
<html>
  <head>
    <title>测试</title>
  </head>
  <body>
    <div class="useful">
      <ul>
        <li class="info">我需要的信息1</li>
        <li class="info">我需要的信息2</li>
        <li class="info">我需要的信息3</li>
      </ul>
     </div>
     <div class="useless">
       <ul>
         <li class="info">垃圾1</li>
         <li class="info">垃圾2</li>
       </ul>
     </div>
  </body>
</html>
'''
selector = lxml.html.fromstring(source)
# info_list = selector.xpath('//div[@class="useful"]/ul/li/text()')
useful = selector.xpath('//div[@class="useful"]')
info_list = useful[0].xpath('ul/li/text()')
print(info_list)
