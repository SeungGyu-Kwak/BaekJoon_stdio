"""
프로그래머 : 곽승규
소속 : 경북대학교 컴퓨터학부
when : 21-01-15
문제 번호 : 1316, 제목 : 그룹 단어 체커
"""

num = int(input())
words_list = list()

for i in range(num):
    words = input()
    words_list.append(words)

count = 0
for w in words_list:
    list_a = []
    check = 0 # 그룹단어 체커 변수
    for j in w:
        if j not in list_a: # list_a리스트에 단어(j)가 없으면
            list_a.append(j)
            prior_word = j # 리스트 마지막에 넣은 문자를 prior_word에 넣는다.
            check = 1
        elif j in list_a and j == prior_word: # list_a에 단어가 있고 그 단어가 이전단어랑 같다면 ! (즉, 같은 단어가 연속으로 나왔다면)
            list_a.append(j)
            prior_word = j
            check = 1
        else:
            check = 0
            break
    if check == 1: # check == 0이면 그룹단어가 아님
        count += 1

print(count)