"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-04
"""
# A+B 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하세요.

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break