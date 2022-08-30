import pymongo
#
from pymongo import ReturnDocument

client = pymongo.MongoClient(host = '192.168.28.142', port = 27017)

db = client.test
collection = db['students']
student = {
    'id': '20170103',
    'name': 'Li',
    'age': 20,
    'gender': 'female'
}

result = collection.insert_one(student)
print(result)
# <pymongo.results.InsertOneResult object at 0x000001B05900FC70>
# 输入-------------------------------------------------------------------------------------
student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name':  'Jordan',
    'age': 20,
    'gender': 'male'
}

result1 = collection.insert_many([student1, student2])
print(result1)
print(result1.inserted_ids) #获取插入数据的_id列表。
# <pymongo.results.InsertManyResult object at 0x000001B05900EBC0>
# [ObjectId('62e9d7ed6dc72c1d8f26b3f7'), ObjectId('62e9d7ed6dc72c1d8f26b3f8')]

# collection.insert_one(student) /// collection.insert_many([student1, student2])

# 查询-------------------------------------------------------------------------------------

result2 = collection.find_one({'name': 'Jordan'})
print(type(result2))
print(result2)
# <class 'dict'>
# {'_id': ObjectId('62e8f6ab47dd0eff0d65bfc4'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}


from bson.objectid import ObjectId

result3 = collection.find_one({'_id': ObjectId('62e9d7ed6dc72c1d8f26b3f7')})
print(result3)
# 结果输出同上46行

result4 = collection.find({'age': 20})
print(result4)
for result in result4:
    print(result)
# 返回所有符合条件值列 - 字典类型

result5 = collection.find({'age':{'$gt':20}}) # 所有大于20年龄的人

result6 = collection.find({'name': {'$regex': '^M.*'}}) # 所有名字以M开头的学生数据

result10 = collection.find( { "$or": [ { 'age': { "$gt": 30 } }, { "name": 'Jordan' } ] } )
for result in result10:
    print(result)
# 多条件并列OR用法!!!!!!!!!!

# 计数-------------------------------------------------------------------------------------
count = collection.estimated_document_count()
count1 = collection.count_documents({'age': 20})
print(count1)
# collection.count()已经弃用
# collection.count_documents()代替 // collection.count_documents({'dt': handle_date})

# 排序-------------------------------------------------------------------------------------

result7 = collection.find().sort('name', pymongo.ASCENDING)
result7 = collection.find().sort('name', -1)
# 1 为升序，-1 为降序，默认为升序。
print([result['name'] for result in result7])

# 偏移-------------------------------------------------------------------------------------
result8 = collection.find().sort('name', pymongo.ASCENDING).skip(11)   # limit(2)
print([result['name'] for result in result8])

# 更新-------------------------------------------------------------------------------------
condition = {'name':'Jordan'}
student = collection.find_one(condition)
student['name']= 'Li'
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

# 指年龄大于20 的第一条符合数据 年龄加1
condition = {'age': {'$gt': 10}}
result = collection.update_one(condition, {'$inc': {'age':3 }})
print(result)
print(result.matched_count, result.modified_count)

# 指年龄大于20 的所有数据 年龄加1
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)

# 删除-------------------------------------------------------------------------------------
result9 = collection.delete_one({'name': 'Jordan', 'age': 20})
print(result9)
# 多条件并列AND用法

result = collection.delete_many({'age': {'$gt': 25}})
print(result.deleted_count)
# delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档：

# collection = db['teacher']   ---- drop() 方法来删除一个集合
# print(collection.drop())

# 组合-------------------------------------------------------------------------------------
Filter = ({'name': 'Li'})
print("The returned document is:")
print(collection.find_one_and_delete(Filter,
                                     projection=None,
                                     sort=None))

# Printing the data in the collection
# after find_one_and_delete() operation.
print("\nThe data after find_one_and_delete() operation is:")

for data in collection.find():
    print(data)

print(collection.find_one_and_replace({'age': 24}, {'age': 99}))

print(collection.find_one_and_update({'name':"Jordan"},
                        { '$set': { "gender" : 'female'} },
                        ))

# 除了name 字段其他都返回
for data in collection.find({}, {'name':0}):
    print(data)