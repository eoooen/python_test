# 序列 [开始位置下标:结束位置下标:步长] 左闭右开

str1 = '012345678'
print(str1[2:5:1])  # 234
print(str1[2:5:2])  # 24
print(str1[2:5])  # 234  默认步长为 1
print(str1[:5])  # 01234 不写开始默认为 0
print(str1[2:])  # 2345678 不写结束默认到最后
print(str1[:])  # 都不写默认输出全部

# 负数测试
print(str1[::-1])  # 步长为负数，表示倒序选取
print(str1[-4:-1])  # 567 下标 -1 为最后一个，依次向前类推

# 终极测试
print(str1[-4:-1:1])  # 567
print(str1[-4:-1:-1])  # 不能选取出数据：从 -4 开始到 -1 结束，选取方向为从左到右，但是 -1 步长；从右向左选取
# **** 如果选取方向和步长的方向冲突，则无法选取数据
print(str1[-1:-4:-1])  # 876
print(str1[6:8:-1])  # 876
