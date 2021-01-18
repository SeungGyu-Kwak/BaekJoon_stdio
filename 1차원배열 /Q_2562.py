"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-05
"""
# 최댓값

list_a = []
for i in range(9):
    num = int(input())
    list_a.append(num)

index_a = 0
max = 0

for index, i in enumerate(list_a):
    if max < i:
        max = i
        index_a = index

print(max)
print(index_a+1)