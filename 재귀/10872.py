"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 22-05-07
"""

def factorial(n):
    result = 1
    if ( n > 0 ):
        return n * factorial(n-1)
    return result

a = int(input())
print(factorial(a))