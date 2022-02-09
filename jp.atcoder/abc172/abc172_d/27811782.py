import typing


def sieve_of_eratosthenes(n: int) -> typing.List[bool]:
    assert n > 1
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    i = 0
    while i * i < n - 1:
        i += 1
        if not is_prime[i]: continue
        for j in range(i * i, n, i):
            is_prime[j] = False
    return is_prime

def least_prime_factor(n: int) -> typing.List[int]:
    is_prime = sieve_of_eratosthenes(n)
    lpf = list(range(n))
    lpf[1] = 0
    i = 0
    while i * i < n - 1:
        i += 1
        if not is_prime[i]: continue
        for j in range(i * i, n, i):
            if lpf[j] == j: lpf[j] = i
    return lpf

def greatest_prime_factor(n: int) -> typing.List[int]:
    lpf = least_prime_factor(n)
    gpf = list(range(n))
    gpf[1] = 0
    for i in range(2, n):
        if lpf[i] == i: continue
        gpf[i] = gpf[i // lpf[i]]
    return gpf

def main() -> typing.NoReturn:
    prime_factorize = PrimeFactorizeLPF(1 << 24)
    n = int(input())
    s = 0
    for k in range(1, n + 1):
        cnt = 1
        for c in prime_factorize(k).values():
            cnt *= (c + 1)
        s += cnt * k
    print(s)


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
