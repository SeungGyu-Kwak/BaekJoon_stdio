"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-05
"""
# 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

num = int(input())

ary1 = list(map(int, input().split()))
print(min(ary1),max(ary1))