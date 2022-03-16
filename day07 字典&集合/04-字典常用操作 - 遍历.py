dict1 = {'name': 'Tom', 'gender': 'man', 'age': '18'}

print('----遍历 key----')
# 遍历 key
for key in dict1.keys():
    print(key)

print('----遍历 values----')
# 遍历 values
for value in dict1.values():
    print(value)

print('----遍历键值对----')
# 遍历键值对
for item in dict1.items():
    print(item)
#
for i, j in dict1.items():
    print(f'{i} = {j}')
