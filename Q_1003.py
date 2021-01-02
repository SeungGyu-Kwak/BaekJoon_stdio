# 피보나치 함수
# 0 1 1 2 3 5 8 13....

C = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]


def one_two_count(n):
    init_len = len(zero)
    if (init_len <= n):
        for i in range(init_len, n + 1):
            add_0 = zero[i - 2] + zero[i - 1]
            add_1 = one[i - 2] + one[i - 1]
            zero.append(add_0);
            one.append(add_1)
    print('{} {}'.format(zero[n], one[n]))


for _ in range(C):
    one_two_count(int(input()))