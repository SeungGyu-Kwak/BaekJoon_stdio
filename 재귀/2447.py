import sys
sys.setrecursionlimit(10**6) # **은 거듭제곱

def draw_stars(n):
    if n == 1: # n을 1까지 도달하게 한 다음 * 리턴
        return ['*']
    Stars = draw_stars(n//3) # //은 몫만 나옴

    L = [] # 리스트 생성

    for star in Stars:
        L.append(star * 3)
    for star in Stars:
        L.append(star + ' ' * (n // 3) + star)
    for star in Stars:
        L.append(star * 3)

    return L

N= int(sys.stdin.readline())
print('\n'.join(draw_stars(N)))


