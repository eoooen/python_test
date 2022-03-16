t1 = ('aa', 'bb', 'cc', 'dd')

# t1[0] = 'aaa'
t2 = ('aa', 'bb', ['cc', 'dd'])
# print(t2[2])
print(t2[2][1])  # dd
t2[2][1] = 'Tom'  # 元组内的第一层数据不可改变，元组内的列表内的数据可以修改
print(t2)
