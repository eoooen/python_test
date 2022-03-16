name_list = ['Tom', 'Lily', 'Rose']
print('--------append--------')  # 结尾追加
name_list.append('Zhangxu')
name_list.append([11, 22])
print(name_list)
# 1、列表是可变数据类型
# 2、追加是序列，则追加整个序列到列表

print('--------extend--------')  # 数据拆开逐一追加
name_list1 = ['Tom', 'Lily', 'Rose']
name_list1.extend('Zhangxu')
name_list1.extend(['Liming', 'Xiaohong'])
print(name_list1)

print('--------insert--------')  # 指定位置新增
# insert(下标位置，增加数据)
name_list2 =  ['Tom', 'Lily', 'Rose']
name_list2.insert(1, 'aaa')
print(name_list2)

print('-------del--------')
name_list3 = ['Tom', 'Lily', 'Rose']
# 1、del
# del name_list3
# del(name_list3)
print(name_list3)
# 2、 可以删除指定下标数据
# del name_list3[0]
print(name_list3)

print('-------pop--------')
# 删除指定下标的数据，如果不指定下标，默认删除最后一个数据
# 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据
# del_name = name_list3.pop(1)
# print(del_name)
# print(name_list3)

print('-------remove--------')
# name_list3.remove('Rose')
# print(name_list3)

print('-------clear------') # 清空列表，留下空列表
name_list3.clear()
print(name_list3)