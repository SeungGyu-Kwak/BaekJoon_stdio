"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-12-31
"""
# 사칙연산

num1 = int(input())
num2 = int(input())

num2_list = []
result_list = []
while num2 != 0:
    i = num2 % 10
    num2_list.append(i)
    num2 = int(num2 / 10)

count = 1
for i in num2_list:
    print(num1 * i)
    result = (num1 * i)*count
    result_list.append(result)
    count *= 10

print(sum(result_list))
