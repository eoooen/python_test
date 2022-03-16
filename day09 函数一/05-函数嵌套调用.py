# 两个函数 TestA 和 TestB -- 在 A 里面嵌套调用 B

# A 函数
def testb():
    print('-----start testb -----')
    print('-----This is testb -----')
    print('-----end testB - ----')

    # A 函数


def testa():
    print('------start testa-------')
    # 起那套调用函数 B
    testb()
    print('------end testa-------')


testa()

