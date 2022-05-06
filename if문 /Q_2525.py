"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 22-04-30
"""

hour, min = map(int, input().split()) # 시간, 분 입력받기
cooking_time = int(input()) # 요리시간 입력받기

if ( min + cooking_time < 60 ): # 2 20 + 30은 그냥 2 50 해주면 됌
    print(hour, min+cooking_time)
elif ( min + cooking_time >= 60 ):# 만약 분이 60분이 넘으면!
    overmin = min + cooking_time # 일단 두 개를 더한다.
    if ( overmin - 60 < 60 ): # 더한 값이 1시간 몇분 일 때는
        if ( hour + 1 == 24 ):
            print(0, overmin - 60)
        else:
            print(hour+1, overmin - 60)
    elif ( overmin - 60 >= 60 ): # 요리하는데 걸리는 분 현재 분이 120분 일 때는! 즉,
        overmin_a = int(overmin / 60) # 시간이 저장될 것이다.
        overmin_b = overmin % 60 # 나누고 나머지가 저장
        result_hour = hour + overmin_a
        if ( result_hour == 24 ):
            print(0, overmin_b)
        elif(result_hour > 24 ):
             print(int(result_hour%24), overmin_b)
        else:
            print(result_hour, overmin_b)



