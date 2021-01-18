"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-14
문제 번호 : 2908, 제목 : 상수
"""

str1, str2 = input().split()

str1 = int(str1[::-1]) # [::-1] : 역순
str2 = int(str2[::-1])

if str1 < str2:
    print(str2)
else:
    print(str1)





