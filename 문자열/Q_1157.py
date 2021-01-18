"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-13
문제 번호 : 1157, 제목 : 단어공부
"""

words = input()
words = words.upper() # 입력받은 문자를 모두 대문자로 바꿔준다.
dic ={} # 딕셔너리 생성
for w in words:
    if w in dic: # 딕셔너리에 단어가 있으면 count 1
        dic[w] += 1
    else: # 없으면 새로 키 : 값 을 생성한다.
        dic[w] = 1

max_value = 0  # 가장 많이 사용된 알파벳의 사용횟수
max_key ='' # 가장 많이 사용된 알파벳 저장할 변수
count = 0

for key, value in dic.items(): # dic.items()로 키, 값을 각각 key, value 변수에 넣는다.
    if value > max_value: # 현재의 max_value보다 크면 최대 값을 바꿔준다.
        max_value = value
        max_key = key
        count = 0 # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우를 체크하기 위해
    elif max_value == value: # 가장 많이 사용된 알파벳의 횟수와 같은 횟수이면 즉, 최대값이 중복이 되는 경우가 있다고 판단.
        count = 1

if count == 0:
    print(max_key)
else: # count == 1이면 최대값이 중복되는 것이므로 ? 출력.
    print("?")