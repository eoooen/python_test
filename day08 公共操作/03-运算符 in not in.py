str1 = 'abcd'
list1 = [10, 20, 30, 40]
t1 = (10, 20, 30, 40)
set1 = {10, 20, 30, 40}
dict1 = {'name': 'Tom', 'id': '001', 'age': '18'}

# in 和 not in
print('a' in str1)  # True
print('e' not in str1)  # True
print('name' in dict1)  # True
print('name' in dict1.keys())  # True
print('Tom' in dict1.values())  # True
print(10 in set1)  # True
