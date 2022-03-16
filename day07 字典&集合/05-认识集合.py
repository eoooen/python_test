# 集合无序
# 集合会去重
# 创建集合只能用 set() 创建

s1 = {10, 20, 30, 40, 50}  # 无序 {40, 10, 50, 20, 30}
print(s1)

s2 = {10, 20, 30, 20, 40, 10}  # 去重 {40, 10, 20, 30}
print(s2)

s3 = set('abcdefg')  # {'f', 'd', 'b', 'g', 'e', 'a', 'c'}
print(s3)

s4 = set()
print(type(s4))  # <class 'set'> 创建空集合

s5 = {}
print(type(s5))  # <class 'dict'>
