"""
for循环可以和 else 配合使用， else 下方缩进的代码指的是当循环正常结束之后要执行的代码

### for else语法

for 临时变量 in 序列：
    重复执行的代码
    ...
else：
    循环正常结束之后要执行的代码

"""
str1 = 'zhangxu'
for i in str1:
    print(i)
else:
    print('循环正常结束之后要执行else代码')