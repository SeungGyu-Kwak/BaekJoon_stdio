"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-02
"""
# 주어진 점이 어느 사분면에 속하는지 알아내는 문제이다.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x > 0 and y < 0:
    print(4)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)