dict1 = {i: i ** 2 for i in range(1, 6)}
print(dict1)

# 将两个列表合并为一个字典
list1 = ['name', 'age', 'gender' 'id']
list2 = ['Tom', '18', 'man']
dict2 = {list1[i]: list2[i] for i in range(len(list2))}
print(dict2)

# 1、如果两个列表的数据相同时，len 统计任何一个列表的长度都可以
# 2、如果两个列表数据个数不同，len 统计数据多的列表数据个数会报错，len 统计数据少的列表数据个数不会报错

# 提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# 提取数量大于 200 字典数据
count1 = {key: value for key, value in counts.items() if key == 200}
print(count1)
