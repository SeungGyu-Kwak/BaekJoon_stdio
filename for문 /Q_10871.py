"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-03
"""
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
num, key = map(int, input().split())

ary = list(map(int, input().split()))

for i in range(num):
    if ary[i] < key:
        print(ary[i], end=" ")

