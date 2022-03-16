# continue: 退出当前一次循环继而执行下一次循环代码
i = 1
while i <= 5:
    # 条件：如果吃到第 4 或 > 3 打印不吃了
    if i == 3:
        print(f'吃饱了，不吃了')
        # 如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

