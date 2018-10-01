import pymongo
import datetime
import time

connection = pymongo.MongoClient()
db = connection.Chapter6
handler_bat = db.Data_bat

start_1_by_1 = time.time()
for row in handler_bat.find():
    old_date = row['time']
    old_time_datetime = datetime.datetime.strptime(old_date, '%Y-%m-%d')
    one_day = datetime.timedelta(days=1)
    new_date = old_time_datetime + one_day
    handler_bat.update({'_id': row['_id']}, {'$set': {'time': str(new_date.date())}}, upsert=False)
end_1_by_1 = time.time()

print(f'逐条更新数据，一共耗时：{end_1_by_1 - start_1_by_1}')


# handler_update_2_insert = db.Data_update_2_insert
# start_update_2_insert = time.time()
# insert_list = []
# for row in handler_bat.find():
#     old_date = row['time']
#     old_time_datetime = datetime.datetime.strptime(old_date, '%Y-%m-%d')
#     one_day = datetime.timedelta(days=1)
#     new_date = old_time_datetime + one_day
#     row['time'] = str(new_date.date())
#     insert_list.append(row)
#
# handler_update_2_insert.insert(insert_list)
# end_update_2_insert = time.time()
#
# print(f'把更新变为插入，共耗时：{end_update_2_insert - start_update_2_insert}')



