"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-12-31
"""

# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

while True:
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print("다시 입력하세요 두 수는 10 이하입니다.")
    else:
        break

result = a * b
print(result)
