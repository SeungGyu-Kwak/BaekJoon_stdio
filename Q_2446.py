# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요

num = int(input())

for i in range(1,num+1):
    print(" " * (i-1) + "*"* (2*num - (2*i-1)))
for i in range(2, num+1):
    print(" " * (num-i) + "*"* (2*i-1))