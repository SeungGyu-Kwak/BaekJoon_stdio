# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

num = int(input())

for i in range(1, num+1):
    print(" "*(num-i) + "*"* i)
for i in range(1,num):
    print(" "* i + "*"*(num-i))