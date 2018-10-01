import csv

# with open('result.csv', encoding='utf-8') as f:
#     reader = [x for x in csv.DictReader(f)]
#
# for row in reader:
#     username = row['username']
#     content = row['content']
#     reply_time = row['reply_time']
#     print('用户名：{}, 回复内容：{}'.format(username, content))

data = [{'name': 'kingname', 'age': 24, 'salary': 99999},
        {'name': 'meiji', 'age': 20, 'salary': 100},
        {'name': '小明', 'age': 30, 'salary': 'N/A'}]
with open('new.csv', 'w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'salary'])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name': '超人', 'age': 999, 'salary': 0})
