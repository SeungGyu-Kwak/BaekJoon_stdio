"""
프로그래머 : Kwaktisu
소속 : KNU CSE
when : 21-01-18
문제 번호 : 2869, 제목 : 달팽이는 올라가고 싶다.
"""
A, B, V = map(int, input().split())
count_day = (V-B)/(A-B)
if count_day == int(count_day):
    print(int(count_day))
else:
    print(int(count_day)+1)