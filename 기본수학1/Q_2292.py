"""
프로그래머 : Kwaktisu
소속 : KNU CSE
when : 20-01-17
문제 번호 : 2292, 제목 : 벌집
"""

num = int(input())

count = 1
i = 0
point = 6
room = 1
if num == 1:
    print(1)
else:
    while True:
        count = count + point
        room += 1
        if num <= count:
            print(room)
            break
        point += 6