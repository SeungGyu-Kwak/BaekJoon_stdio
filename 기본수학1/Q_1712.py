"""
프로그래머 : Kwaktisu
소속 : KNU CSE
when : 21-01-17
문제 번호 : 1712, 제목 : 손익분기점
"""

A, B, C = map(int, input().split())

if B >= C: # 즉, 가변 비용이 판매비용보다 비싸면 손익분기점을 넘길 수 없음.
    print(-1)
else:
    print(int(A/(C-B) + 1))