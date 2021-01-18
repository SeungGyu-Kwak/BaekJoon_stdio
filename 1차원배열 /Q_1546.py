"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-07
"""
# 평균
from sys import stdin

num = int(stdin.readline())
ary1 = list(map(int, stdin.readline().split()))

max_num = max(ary1)

for i in range(num):
    ary1[i] = ary1[i]/max_num*100

avg = sum(ary1)/num
print("%.2f" % avg)