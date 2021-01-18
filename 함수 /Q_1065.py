"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-07
문제 번호 : 1065, 제목 : 한수
"""


num = int(input())

hansu = 0
for i in range(1, num+1):
    if i <= 99:
        hansu += 1
    else:
        list_a = list(map(int,str(i)))
        if list_a[0] - list_a[1] == list_a[1] - list_a[2]:
            hansu += 1

print(hansu)
