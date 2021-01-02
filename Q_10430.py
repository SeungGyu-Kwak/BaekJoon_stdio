"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-12-31
"""
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a,b,c = map(int, input().split())
result1 = (a+b) % c
result2 = ((a % c) + ( b % c))% c
result3 = (a * b )%c
result4 = ((a%c) * (b%c))%c

print(result1)
print(result2)
print(result3)
print(result4)

