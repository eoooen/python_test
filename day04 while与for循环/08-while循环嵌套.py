"""
1. 循环打印三次aaa
2. 另一件事
3. 上面是一套惩罚，这一套惩罚重复执行三天 -- 一套惩罚要重复执行 -- 放到一个while循环里面
"""
import random

j = 0
while j < 3:
    i = 0
    while i < 11:
        a = random.randint(0, 9)
        print(a, end="")
        i += 1
    print()
    print('以上为学号')
    j += 1
    print(f'第{j}天惩罚结束\n----------------------')
print('所有惩罚结束!!!')
