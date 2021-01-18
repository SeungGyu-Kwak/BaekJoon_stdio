"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-05
"""
# 나머지

list_a = []
for i in range(10):
    list_a.append(int(input()))

list_b = []
count = 0
for i in range(10):
    num = list_a[i] % 42
    if num not in list_b:
        list_b.append(num)
print(len(list_b))