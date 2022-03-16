str1 = 'zhangxu'
for i in str1:
    if i == 'g':
        print('遇到g不执行')
        continue  # 循环遇到continue，正常终止，else下代码执行
    print(i)
else:
    print('循环正常结束之后要执行else代码')