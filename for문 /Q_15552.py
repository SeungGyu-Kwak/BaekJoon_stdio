"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-03
"""
# 빠른 A+B
import sys

num = int(input())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    # sys.stdin.readline().split()을 통해 한 라인을 입력받은 후 split()함수를 통해 띄어쓰기 기준으로 나누고
    # map 함수를 통해 a,b에 각각 저장한다.
    print(a+b)