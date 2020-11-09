"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
"""

num = int(input())
input_array = []
dp = []
for i in range(num):
    input_array.append(int(input()))

max_value = max(input_array)
# print(max_value)

for i in range(max_value+1):
    if i == 0 or i == 1:
        dp.append(1)
    elif i == 2:
        dp.append(2)
    else:
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in input_array:
    print(dp[i])