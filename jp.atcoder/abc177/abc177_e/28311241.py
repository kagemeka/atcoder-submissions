import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    # if gcd(a_i, a_j) = 1 for all pairs (i, j),
    # there is no coprime between any pair (a_i, a_j).
    # otherwise if gcd(a_0, a_1, ..., a_{n-1}) = 1, each coprime factor included in at most (n - 1) values.

    k = 1 << 20
    cnt = [0] * k
    for x in a:
        for i in range(2, x + 1):
            if i * i > x: break
            if x % i: continue
            cnt[i] += 1
            while x % i == 0: x //= i
        if x > 1: cnt[x] += 1


    if max(cnt) == 1:
        print('pairwise coprime')
    elif max(cnt) <= n - 1:
        print('setwise coprime')
    else:
        print('not coprime')

main()
