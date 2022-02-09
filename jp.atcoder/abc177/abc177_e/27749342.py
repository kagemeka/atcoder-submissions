import typing


import collections

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    appeared_cnt = collections.defaultdict(int)
    for x in a:
        for p in prime_factorize(x):
            appeared_cnt[p] += 1
    cnt = appeared_cnt.values()
    if max(cnt) == 1:
        print('pairwise coprime')
    elif max(cnt) < n:
        print('setwise coprime')
    else:
        print('not coprime')



def prime_factorize(n: int) -> typing.DefaultDict[int, int]:
    import collections
    cnt = collections.defaultdict(int)
    i = 1
    while i * i < n:
        i += 1
        while n % i == 0:
            n //= i
            cnt[i] += 1
    if n > 1: cnt[n] = 1
    return cnt


main()
