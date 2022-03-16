# 可以存储多个数据，可以不同类型
name_list = ['Tom', 'Lily', 'Rose']

print(name_list)
print(name_list[0])  # Tom
print(name_list[1])  # Lily
print(name_list[2])  # Rose

print('-------index------')
print(name_list.index('Lily', 0, 2))  # 返回下标 1
print(name_list.index('Rose'))  # 返回下标 2
# print(name_list.index('ggg'))  # 找不到报错

print('----------count--------')
print(name_list.count('Tom'))  # 1 次
print(name_list.count('Liming'))  # 0 次

print('----------len--------')
print(len(name_list))  # 3 个数据

print('--------判断--------')
print('Tom' in name_list)  # True
print('Toms' in name_list)  # False
print('Rose' not in name_list)  # False
print('Roses' not in name_list)  # True

print('--------example------')
# 判断用户是否存在，如果存在，提示用户，否则提示可以注册
while True:
    name = input('please input your name:')

    if name in name_list:
        print(f'your input name is {name},This name is exist!!!')
    else:
        print(f'your input name is {name},You can register')
        exit()
