dict1 = {'name': 'Tom', 'gender': 'man', 'age': '18'}
# 1、key
print(dict1['name'])  # Tom

# 2、函数
# 2、1 字典序列.get(key, 默认值)  如果查找的 key 不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None
print(dict1.get('name'))  # Tom
print(dict1.get('names'))  # None
print(dict1.get('id', 100))  # 100

# 2、2 keys()  查找字典中的所有 key，返回可迭代对象
print(dict1.keys())  # dict_keys(['name', 'gender', 'age'])

# 2、3 values() 查找字典中的所有 values，返回可迭代对象
print(dict1.values())  # dict_values(['Tom', 'man', '18'])

# 2、4 items() 查找字典中的所有键值对，返回可迭代对象，里面的数据是元组，元组数据 1 是字典的 key，元组数据 2 是字典的 key 对应的 values
print(dict1.items())  # dict_items([('name', 'Tom'), ('gender', 'man'), ('age', '18')])
