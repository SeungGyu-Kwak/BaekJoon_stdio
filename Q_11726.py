"""
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다
"""
n = int(input())
ary = []
for i in range(n+1):
    if i == 0:
        ary.append(1)
    elif i == 1:
        ary.append(1)
    else:
        ary.append(ary[i-2] + ary[i-1])

result = ary[n]

print(result % 10007)