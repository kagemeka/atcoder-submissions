import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    # if gcd(a_i, a_j) = 1 for all pairs (i, j),
    # there is no coprime between any pair (a_i, a_j).
    # otherwise if gcd(a_0, a_1, ..., a_{n-1}) = 1, each coprime factor included in at most (n - 1) values.

    k = 1 << 20
    lpf = list(range(k))
    for i in range(2, k):
        if i * i >= k: break
        if lpf[i] != i: continue
        for j in range(i * i, k, i):
            if lpf[j] == j: lpf[j] = i


    cnt = [0] * k
    for x in a:
        while x > 1:
            p = lpf[x]
            cnt[p] += 1
            while x % p == 0: x //= p


    if max(cnt) <= 1:
        print('pairwise coprime')
    elif max(cnt) <= n - 1:
        print('setwise coprime')
    else:
        print('not coprime')

main()
