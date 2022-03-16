age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

print("my age is %d" % age)
print("my name is %s" % name)
print("my weight is %.2fkg" % weight)               # %与f之间加.2f，就可以保留2位小数
print("my class number is %d" % stu_id)
print("my class number is %03d" % stu_id)           # %与d之间加上03d，就可以显示3位，不足用0补齐
print('my name is %s, age is %d' % (name, age))     # 输出多个变量，用括号括起来，逗号隔开依次填写
print('my name is %s, next age is %d' % (name, age + 1))
print('my name is %s, age is %d, weight is %.2f, class number is %06d' % (name, age, weight, stu_id))

