"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-02
"""
# 알람시계
H , M = map(int, input().split())

M1 = M+15
if M1 < 60:
    if H == 0:
        print(23, M1)
    else:
        print(H-1, M1)
elif M1 == 60:
    print(H, 0)
else:
    print(H, M1-60)

