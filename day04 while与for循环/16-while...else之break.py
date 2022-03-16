i = 0
while i < 5:
    if i == 3:
        break  # 循环遇到break，循环非正常终止，else下代码不执行
    print('对不起！')
    i += 1
else:
    print('原谅你了！')
