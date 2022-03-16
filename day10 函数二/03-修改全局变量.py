# B 函数想要 a 的取值是 200
a = 100

print(a)


def testa():
    print(a)


def testb():
    a = 200  # 此处 a 是局部变量，修改不会改变全局变量
    print(a)


testa()  # 100
testb()  # 200
print(a)  # 100 调用的是全局变量


# 修改全局变量

def testc():
    # 想要在函数体内部修改全局变量 a：值是 200
    global a
    a = 200
    print(a)


testc()
print(a)  # 此时修改了全局变量 a 的值
