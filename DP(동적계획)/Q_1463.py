"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시요.
"""

n = int(input())
count = 0
minimum = [n]
def cal(a):
    list_a = []
    for i in a:
        list_a.append(i-1)
        if i%3 == 0:
            list_a.append(i/3)
        if i%2 == 0:
            list_a.append(i/2)
    return list_a

while True:
    if n == 1:
        print(count)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count +=1
    if min(minimum) == 1:
        print(count)
        break






