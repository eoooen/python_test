"""
1. 书写input
    input（'提示信息'）

2. 观察特点
    2.1 遇到input，等待用户输入
    2.2 接收input存变量
    2.3 input接收到的数据类型都是字符串
"""

password = input('Please input your password:')
print(f'{password}')

print(type(password))
