while True:
    age = int(input('please input your age:'))
    # sex = input('please intput your sex:')
    if age < 18:
        print('你的年龄太小，是童工！')
    elif (age >= 18) and (age <= 60):
        print('你可以进行工作！')
    # elif sex == "men":
    #     print(f 'your sex is {sex}, you can play many games!!!')
    elif 60 < age <= 100:
        print('你的年龄太大，你该休息了！')
    else:
        exit(10)
