# find()：检测某个子串是否包含在这个字符串中，如果在返回这个字符串开始的位置下标，否则则返回 -1
# 语法
# 字符串序列.find(子串，开始位置下标，结束位置下标） 开始和结束的下标可以省略

# find
mystr = "hello world and Python and China"
print(mystr.find('and'))  # 12
print(mystr.find('and', 13, 30))  # 23
print(mystr.find('and', 15, 20))  # -1
print(mystr.find('ands'))  # -1 查找不存在返回 -1

# index
print(mystr.index('and'))  # 12
print(mystr.index('and', 13, 30))  # 23
# print(mystr.index('and', 15, 20))  # 查找不存在报错

# count
print(mystr.count('and', 15, 30))  # 1 个
print(mystr.count('and'))  # 2 个
print(mystr.count('ands'))  # 0 个

# rfind 从右边查找
# rindex 从右边查找

