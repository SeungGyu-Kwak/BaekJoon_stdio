"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-05
"""
# 숫자의 개수
a = int(input())
b = int(input())
c = int(input())
mul_value = a * b *c

result = list(str(mul_value))
for i in range(10):
    print(result.count(str(i)))

