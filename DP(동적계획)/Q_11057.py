# 오르막 수
# 오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
# 수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

# 1000 X 10 배열 만들기

if __name__=="__main__":
    num = int(input())
    DP = [[0 for col in range(10)] for row in range(num+1)]

    for i in range(num+1):
        if i == 0:
            continue
        for j in range(10):
            if i == 1:
                DP[i][j] = 1
            if j == 0:
                DP[i][j] = 1
            else:
                DP[i][j] = DP[i][j-1] + DP[i-1][j]

    sum = 0
    for i in range(10):
        sum += DP[num][i]

    result = sum % 10007
    print(result)


