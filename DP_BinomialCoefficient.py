# 동적계획방법을 사용하여 이항계수를 구하는 알고리즘을 만들어 보자.

def minimum(a,b):
    if a < b:
        return a
    else:
        return b

def bin2(n, k):
    B = [[0 for col in range(k+1)] for row in range(n+1)] # 2차원 리스트 생성
    for i in range(0, n+1):
        for j in range(0, minimum(i,k)+1):
            if ( j == 0 or j == i):
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    # for i in B:
    #     for j in i:
    #         print(j, end=" ")
    #     print()
    return B[n][k]

if __name__=="__main__":
    n, k = map(int, input("찾고싶은 이항계수를 적으세요 (ex)4 2 : ").split())
    result = bin2(n, k)

    print(result)
