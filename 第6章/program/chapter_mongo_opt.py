import pymongo
import datetime
import random
import time

connection = pymongo.MongoClient()
db = connection.Chapter6
handler_1_by_1 = db.Data_1_by_1
handler_bat = db.Data_bat

today = datetime.date.today()

#逐条插入数据
# start_1_by_1 = time.time()
# for i in range(10000):
#     delta = datetime.timedelta(days=i)
#     fact_date = today - delta
#     handler_1_by_1.insert({'time': str(fact_date), 'data': random.randint(0, 10000)})
# end_1_by_1 = time.time()

#批量插入数据
start_bat = time.time()
insert_list = []
for i in range(10000):
    delta = datetime.timedelta(days=i)
    fact_date = today - delta
    insert_list.append({'time': str(fact_date), 'data': random.randint(0, 10000)})

handler_bat.insert(insert_list)
end_bat = time.time()

# print(f'一条一条插入数据，耗时：{end_1_by_1 - start_1_by_1}')
print(f'批量插入数据，耗时: {end_bat - start_bat}')
