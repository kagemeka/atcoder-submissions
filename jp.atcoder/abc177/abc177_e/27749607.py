import typing


import collections

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    prime_factorize = PrimeFactorizeLPF(1 << 20)
    cnt = [0] * (1 << 20)
    for x in a:
        for p in prime_factorize(x).keys():
            cnt[p] += 1
    mx = max(cnt)
    if mx <= 1:
        print('pairwise coprime')
    elif mx < n:
        print('setwise coprime')
    else:
        print('not coprime')



def least_prime_factor(n: int) -> typing.List[int]:
    assert n > 1
    s = list(range(n))
    s[0] = s[1] = -1
    i = 0
    while i * i < n - 1:
        i += 1
        if s[i] != i: continue
        for j in range(i * i, n, i):
            if s[j] == j: s[j] = i
    return s


class PrimeFactorizeLPF():
    def __call__(self, n: int) -> typing.DefaultDict[int, int]:
        import collections
        cnt = collections.defaultdict(int)
        while n > 1:
            p = self.__lpf[n]
            n //= p
            cnt[p] += 1
        return cnt

    def __init__(self, n: int) -> typing.NoReturn:
        self.__lpf = least_prime_factor(n)



main()
