# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

string_a = input()

string_len = len(string_a) # 문자열 길이
for i in range(0,string_len, 10): # 0부터 string_len-1까지 10의 범위로 출력.
    b = i + 10
    print(string_a[i:b]) # [i:b] 는 i부터 b-1까지의 인덱스를 출력해라는 뜻