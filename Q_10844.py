# 45656이란 수를 보자. 이 수는 인접한 모드 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오.

num = int(input())

DP = [[0 for col in range(10)] for row in range(101)] # dp배열 생성 후 0으로 초기화

for i in range(10):
    if i == 0:
        continue
    else:
        DP[1][i] = 1

for i in range(2, num+1):
    for j in range(10):
        if j == 0:
            DP[i][j] = DP[i-1][j+1]
        elif j == 9:
            DP[i][j] = DP[i-1][j-1]
        else:
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
#
# for i in DP:
#     for j in i:
#         print(j, end=" ")
#     print()

sum = 0
for i in range(10):
    sum += DP[num][i]

result = sum % 1000000000
print(result)