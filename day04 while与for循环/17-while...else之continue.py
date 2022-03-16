i = 0
while i < 5:
    if i == 3:
        i += 1
        print('这次不真诚')
        continue  # 循环遇到continue，正常终止，else下代码执行
    print('对不起！')
    i += 1
else:
    print('原谅你了！')
