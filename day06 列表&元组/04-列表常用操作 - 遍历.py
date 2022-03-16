name_list = ['Tom', 'Lily', 'Rose']
"""
 1、准备表示下标数据
 2、循环 while
  条件 i < 3  len()
  遍历：依次按顺序访问到序列的每一个数据
  i += 1
"""
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# for 循环遍历
for i in name_list:
    print(i)
