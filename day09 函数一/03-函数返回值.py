# 定义一个函数：返回 烟
def buy():
    return '烟'
    print('Ok')


gooes = buy()
print(gooes)  # 烟
"""
return 作用：
1、负责函数返回值
2、退出当前函数，导致 return 下方的所有代码（函数体内部）不执行
"""


# return 返回的结果给函数调用的地方
def add_num(a, b):
    return a + b


# 用 result 存储返回值
result = add_num(10, 20)
print(result)
