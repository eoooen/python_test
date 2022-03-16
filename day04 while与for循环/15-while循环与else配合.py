"""
while循环可以和 else 配合使用， else 下方缩进的代码指的是当循环正常结束之后要执行的代码

### while else语法

while 条件：
    条件成立重复执行的代码
else：
    循环正常结束之后要执行的代码

"""
i = 0
while i < 3:
    print('对不起！')
    i += 1
else:
    print('原谅你了！')
