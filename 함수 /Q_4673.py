"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 20-01-07
문제 번호 : 4673, 제목 : 셀프넘버
"""
def d(n):
    list_a = []
    value = n
    while n != 0:
        result = n % 10
        list_a.append(result)
        n = int(n / 10)
    value += sum(list_a)
    return value

result_list = []

for i in range(1,10001):
    result1 = d(i)
    result_list.append(result1)

for i in range(1,10001):
    if i not in result_list:
        print(i)




