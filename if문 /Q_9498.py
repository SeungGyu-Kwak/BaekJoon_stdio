"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-02
"""
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

score = int(input())
if (90<=score and score <= 100):
    print("A")
elif ( 80 <= score and score < 90):
    print("B")
elif ( 70 <= score and score < 80):
    print("C")
elif ( 60 <= score and score < 70):
    print("D")
else:
    print("F")