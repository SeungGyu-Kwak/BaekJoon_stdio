# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

num = int(input())


for i in range(num):
    sum = 0
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    print("Case #%d: %d + %d = %d" % (i+1, num1, num2, sum))

