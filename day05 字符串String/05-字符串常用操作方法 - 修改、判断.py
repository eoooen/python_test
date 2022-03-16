# replace(): 替换
# 字符串序列.replace(旧子串，新子串，修改次数）

print('--------replace-------')
# replace() 步 and 替换成 he 说明 replace 函数有返回值，返回值是修改后的字符串
# 替换次数超出子串出现的次数，表示替换所有子串

mystr = "hello world and Python and China"
new_mystr = mystr.replace('and', 'he', 10)
print(new_mystr)
# ***** 调用了 replace 函数后，发现原有字符串的数据并没有做到修改，修改后的数据是 replace 函数的返回值
# 说明：字符串是不可变数据类型
# 数据是否可以改变划分为 可变类型 和 不可变类型

print('-------split---------')
# split() 分割，返回一个列表,丢失分割字符
# 字符串序列.split(分割符, num)

list1 = mystr.split(' ')
list2 = mystr.split('and', 1)
print(list1)
print(list2)

print('---------join-------')
# join() 用一个字符或子串合并字符串，合并列表里面的字符串为一个大字符串
# 字符或子串.join(多字符串组成的序列)

mylist = ['aa', 'bb', 'cc']
new_mylist = '...'.join(mylist)
print(new_mylist)

print('---------大小写转换----------')
print(mystr.capitalize())  # 字符串首字母大写
print(mystr.title())  # 单词首字母大写
print(mystr.upper())  # 小写转大写
print(mystr.lower())  # 大写转小写

print('---------删除空白字符-------')
mystr1 = '   hello world   '
print(mystr1)
print(mystr1.lstrip())  # 删除左侧空白字符
print(mystr1.rstrip())  # 删除右侧空白字符
print(mystr1.strip())  # 删除两侧空白字符

print('--------左中右对齐--------')
# 返回原字符进行左中右对齐，并使用指定的字(默认空格)填充至对应的长度的新字符串
mystr2 = 'hello'
print(mystr2.ljust(10))
print(mystr2.ljust(10, '.'))  # 左对齐不足用 . 补齐
print(mystr2.rjust(10, '.'))  # 右对齐不足用 . 补齐
print(mystr2.center(11, '.')) # 10个字符剧中对齐，不足用 . 对齐

print('-------判断-------')
# startwith(子串，开始位置下标，结束位置下标)
mystr3 = 'hello this is my new friend'
print(mystr3.startswith('he'))
print(mystr3.startswith('hello'))
print(mystr3.startswith('e', 1, 10))
# endswith(子串，开始位置下标，结束位置结束)】
print(mystr3.endswith('friend'))
print(mystr3.endswith('end'))
print(mystr3.endswith('en', -3, -1))




