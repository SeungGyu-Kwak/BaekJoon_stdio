"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-07
문제 번호 : 4344, 제목 : 평균은 넘겠지
"""
num = int(input())
for i in range(num):
    ary1 = list(map(int, input().split()))
    avg = sum(ary1[1:]) / ary1[0]
    count = 0
    for j in ary1[1:]:
        if avg < j:
            count += 1
    ratio = count/ary1[0]*100
    print('%.3f' % ratio,'%', sep='')
