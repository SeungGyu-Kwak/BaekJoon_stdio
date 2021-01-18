"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-15
문제 번호 : 5622, 제목 : 다이얼
"""

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ary1 = input()

time = 0
for i in dial:
    for j in ary1:
        if j in i:
            time += dial.index(i) + 3 # index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
print(time)