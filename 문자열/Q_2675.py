"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-13
문제 번호 : 2675, 제목 : 문자열반복
"""

T = int(input())

for i in range(T):
    R, S = list(input().split())
    R = int(R)
    text = ''
    for j in S:
        text += R*j
    print(text)
