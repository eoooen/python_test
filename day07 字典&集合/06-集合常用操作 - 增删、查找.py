s1 = {10, 20}
# add
# 1、集合是可变类型
s1.add(100)
print(s1)
# 2、集合有去重功能，如果追加的数据是集合已有数据，则什么事情都不用做
s1.add(100)
print(s1)
# 3、s1.add([10， 20， 30])
# s1.add([10， 20， 30]) # 报错，add 无法添加序列
# print(s1)

# update 追加的数据是序列
s1.update([10, 20, 30])
print(s1)

s2 = {10, 20, 30, 40}
# remove 删除指定的数据，数据不存在会报错
s2.remove(10)
print(s2)
# s2.remove(10)

# discard 删除指定的数据，数据不存在不会报错
s2.discard(10)  # 不报错
print(s2)
# pop 删除随机的数据，删除的数据会返回
del_num = s2.pop()
print(del_num)

# 查找 in not in
s3 = {10, 20, 30, 40}
print(10 in s3)  # True
print(10 not in s3)  # False
