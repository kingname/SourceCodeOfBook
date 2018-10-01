from pymongo import MongoClient
client = MongoClient()
database = client['Chapter6']
collection = database['spider']

# 写入数据
data = {'id': 123, 'name': 'kingname', 'age': 20, 'salary': 999999}
collection.insert(data)

more_data = [
    {'id': 2, 'name': '张三', 'age': 10, 'salary': 0},
    {'id': 3, 'name': '李四', 'age': 30, 'salary': -100},
    {'id': 4, 'name': '王五', 'age': 40, 'salary': 1000},
    {'id': 5, 'name': '外国人', 'age': 50, 'salary': '未知'},
]

collection.insert(more_data)

# 查询数据
# content = [x for x in collection.find({'age': 29}, {'_id': 0, 'name': 1, 'salary': 1})]
# content_obj = collection.find({'age': 29}, {'_id': 0, 'name': 1, 'salary': 1})
# content = []
# for each in content_obj:
#     content.append(each)


# 逻辑查询
# content = [x for x in collection.find({'age': {'$gte': 29, '$lte': 40}})]

#排序
# content = [x for x in collection.find({'age': {'$gte': 29, '$lte': 40}}).sort('age', -1)]
# content = [x for x in collection.find({'age': {'$gte': 29, '$lte': 40}}).sort('age', 1)]

# 去重
# content = collection.distinct('age')
# print('finished')