"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-02
"""
# 두 정수 A와 B가 주어졌을 대, A와 B를 비교하는 프로그램을 작성하시오.
a, b = map(int, input().split())

if ( a < b ):
    print("<")
elif ( a > b ):
    print(">")
else:
    print("==")