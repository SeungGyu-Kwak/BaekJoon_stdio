"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-04
"""
# 더하기 사이클
num = int(input())
count = 0
check = num
temp = 0
new_num = 0

while True:
    temp = num//10 + num % 10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break

print(count)