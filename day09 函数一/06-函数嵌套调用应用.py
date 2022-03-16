# 1、打印一条横线
def print_line():
    print('-' * 20)


# 嵌套调用打印一条横线，实现打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_lines(3)


# 2、函数做数学计算
def sum_num(a, b, c):
    return a + b + c


result = sum_num(10, 20, 30)
print(result)


def average_num(a, b, c):
    sumResult = sum_num(a, b, c)
    return sumResult / 3


averageResult = average_num(10, 20, 30)
print(averageResult)
