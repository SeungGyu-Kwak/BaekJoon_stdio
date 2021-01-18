"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-15
문제 번호 : 2941, 제목 : 크로아티아 알파벳
"""

a = ['c=', 'c-', 'dz=', 'd-','lj','nj','s=','z='] # 크로아티아 알파벳
ary1 = input()

for i in a:
    ary1 = ary1.replace(i,'*')

print(len(ary1))
