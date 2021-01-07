"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-07
"""
# OX퀴즈

num = int(input())

result_list = []
for i in range(num):
    count = 0
    sum = 0
    ary1 = list(input())
    # print(ary1)
    for j in ary1:
        if j == 'O':
            count += 1
            sum += count
        else:
            count = 0
            sum += count
    result_list.append(sum)

for i in result_list:
    print(i)