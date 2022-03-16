# break: 当某些条件成立，终止整个循环
i = 1
while i <= 5:
    # 条件：如果吃到第 4 或 > 3 打印不吃了
    if i == 4:
        print(f'吃饱了，不吃了')
        break

    print(f'吃了第{i}个苹果')
    i += 1
