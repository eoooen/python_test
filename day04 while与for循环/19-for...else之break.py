str1 = 'zhangxu'
for i in str1:
    if i == 'g':
        break  # 循环遇到break，循环非正常终止，else下代码不执行
    print(i)
else:
    print('循环正常结束之后要执行else代码')
