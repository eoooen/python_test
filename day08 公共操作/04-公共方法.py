str1 = 'adcde'
list1 = [10, 20, 30]
dict1 = {'name': 'Tom', 'id': '001', 'age': '18'}
# 适用于所有数据类型
# len() 计算容器元素的个数
# del del() 删除
# del str1
# print(str1)
del list1[0]
print(list1)
del(dict1['name'])
del dict1['age']
print(dict1)

# max() 返回容器中的最大值
print(max(str1))
print(max(list1))
# min() 返回容器中的最小值
print(min(str1))
# rang(start,end,step) 生成从start到end的数字，步长为step，供for循环使用,左闭右开
for i in range(0,10): # 0 1 2 3 4 5 6 7 8 9
    print(i, end=' ')
for j in range(1, 9, 2): # 3 5 7
    print(j)

# enumerate() 函数用于将一个可遍历的数据对象（如列表、元组或字符串）组合成一个索引序列，同时列出数据和数据下标，一般用在for循环当中
# enumerate(可遍历对象，start=0) start 参数用来设置遍历数据的下标起始值，默认为 0
list2 = [10, 20, 30, 40 , 50, 60]

# enumerate 返回的数据是元组，元组的第一个数据是原迭代数据对应的下标，元组的第二个数据是原迭代对象的数据

for i in enumerate(list2, start=1):
    print(i)



