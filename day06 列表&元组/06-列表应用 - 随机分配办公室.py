# 需求 8 位老师，3 个办公室，8 位老师分配到 3 个办公室
"""
1、准备数据
    1、1 8 位老师 -- 列表
    1、2 3 个办公室 -- 列表嵌套
2、 分配老师到办公室
    随机分配
    把老师名字写到办公室列表 -- 办公室列表追加老师名字数据
3、 验证
"""

import random
# 1、准备数据
teachers  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], []]
# 2、分配老师到办公室
for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

# print(office)
i = 1
for office in offices:
    print(f'第{i}个办公室的人数是{len(office)}位,每个办公室的老师分别是:')
    i += 1
    for name in office:
        print(name, end=" ")
    print()