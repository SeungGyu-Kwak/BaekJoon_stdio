"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-12-31
"""
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

a, b = map(int, input().split())
result_sum = a+b
result_sub = a-b
result_mul = a*b
result_div = int(a/b)
result_na = a%b

print(result_sum)
print(result_sub)
print(result_mul)
print(result_div)
print(result_na)