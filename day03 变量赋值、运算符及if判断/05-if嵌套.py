money = 1
site = 1
if money == 1:
    print('请上车')
    # 判断能否坐下
    if site == 1:
        print('有空座，可以坐下')
    else:
        print('没有空座，站着等')
else:
    print('没有钱，不能上车')
