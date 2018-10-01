with open('text.txt', encoding='utf-8') as f:
    content_list = f.read()
    print(content_list)

with open('new.txt', 'w', encoding='utf-8') as f:
    f.write('你好')
    f.write('\n===============\n')
    f.writelines(['嘿嘿', '跟我学爬虫'])
    f.write('\n===============\n')
    f.writelines(['爬虫开发\n', '看这本书就够了\n'])

