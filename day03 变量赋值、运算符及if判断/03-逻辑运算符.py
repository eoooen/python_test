a = 0
b = 1
c = 2

# 1. and: 与：都真才真
print((a < b) and (c > b))
print(a > b and c > b)

# 2. or：或：一真就真，都假才假
print(a < b or b < c)
print(a > b or b > c)

# 3. not：非：取反
print(not False)
print(not c > b)

# and运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
print(a and b)  # 0
print(b and a)  # 0
print(a and c)  # 0
print(c and a)  # 0
print(b and c)  # 2
print(c and b)  # 1

# or运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
print(a or b)  # 1
print(a or c)  # 2
print(b or c)  # 1
print(a or a)  # 0
