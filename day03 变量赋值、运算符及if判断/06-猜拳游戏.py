"""
1. 出拳
    玩家：手动输入
    电脑：1. 固定：剪刀 2. 随机
2. 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""
# 1. 出拳
# 玩家
import random

while True:
    player = int(input('请除出拳：0--石头；1--剪刀；2--布:'))
    # 电脑
    # computer = 1
    computer = random.randint(0, 2)  # 包含0与2
    # print(computer)
    # 判断输赢
    if ((player == 0) and (computer == 1)) or \
            ((player == 1) and (computer == 2)) or \
            ((player == 2) and (computer == 0)):
        print('<^-^>玩家获胜<^-^>')
    # 平局
    elif player == computer:
        print('平局,再来一局。')
    # 电脑获胜
    else:
        print('电脑获胜')
