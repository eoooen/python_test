# 适用列表、字典、集合
# 1、准备一个空列表
list1 = []
list2 = []
# 2、书写循环，依次追加数字到空列表 list1 中
# while
i = 0
while i < 10:
    list1.append(i)
    i += 1

print(list1)
# for
for i in range(0,10):
    list2.append(i)

print(list2)

# 列表推导式
list3 = [i for i in range(0,10)]
print(list3)

# 使得列表内全为偶数
list4 = []
# list4 = [i for i in range(0,10,2)] # 使用步长进行控制

#使用 for 循环进行控制
# for i in range(0,10):
#     if i % 2 == 0:
#         list4.append(i)

# list4 = [i for i in range(0,10) if i % 2 == 0] # 带 if 列表推导式
# print(list4)

# 多个 for 循环实现列表推导式
# 需求：list5 = [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# list5 = []
# for i in range(1,3):
#     for j in range(3):
#         list5.append((i, j))
# print(list5)
# 多个 for 实现列表推导式
list5 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list5)

