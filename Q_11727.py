"""
2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×17 직사각형을 채운 한가지 예이다.
"""
n = int(input())
ary = []
for i in range(n+1):
    if i == 0 or i == 1:
        ary.append(1)
    else:
        ary.append(ary[i-1] + ary[i-2]*2)

result = ary[n]
print(result % 10007)