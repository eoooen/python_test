# 全局变量，指在函数体内、外都能生效的变量
a = 100

print(a)  # 函数体外访问

def testa():
    print(a)


def testb():
    print(a)


testa()  # 100 函数体内访问
testb()  # 100 函数体内访问


