str1 = 'zhangxu'
for i in str1:
    # 当某些条件条件退出循环 -- break：条件 i 取到字符 g
    if i == 'g':
        print('遇到 g 退出循环')
        break
    print(i)
