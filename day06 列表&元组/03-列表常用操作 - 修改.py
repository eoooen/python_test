name_list = ['Tom', 'Lily', 'Rose']
# 1、修改指定下标数据
name_list[0] = 'aaa'
print(name_list)


# 2、逆序 reverse
list1 = [1, 3, 2, 5, 4, 6]
# list1.reverse()
# print(list1)


# 3、sort(key=None, reverse=False) reverse=True降序，reversr=False 升序（默认）
list1.sort(reverse=False)
print(list1)
list1.sort(reverse=True)
print(list1)

# copy()
name = ['aa', 'bb', 'cc']
name1 = name.copy()
print(name1)
