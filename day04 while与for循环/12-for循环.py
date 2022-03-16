"""
###for 循环语法###

for 临时变量 in 序列：
    重复执行的代码1
    重复执行的代码2
    ......
"""
a = [1, 2, 3, 4, 5, 6]
str1 = 'zhangxu'
for i in str1:
    print(i)
    # for j in str1:
    #     print(f'{j}', end=" ")
    # print()
row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
