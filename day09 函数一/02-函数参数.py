# 1、函数：固定数据 1 和 2 加法
def add_unm1():
    result = 1 + 2
    print(result)


add_unm1()


# 2、函数：参数形式传入实际数据进行加法
def add_num2(a, b, c):  # a, b, c 形参
    result = a + b
    total1 = a * b + c
    print(result, total1)


add_num2(10, 20, 100)  # 实参
add_num2(10, 20)  # 报错，定义函数有 3 个参数，传入参数也要是 3 个
