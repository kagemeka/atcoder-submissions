import typing



def cumprod(mod: int, a: typing.List[int]) -> typing.List[int]:
    a = a.copy()
    for i in range(len(a) - 1):
        a[i + 1] = a[i + 1] * a[i] % mod
    return a


def factorial(mod: int, n: int) -> typing.List[int]:
    fact = list(range(n))
    fact[0] = 1
    return cumprod(mod, fact)


def factorial_inverse(p: int, n: int) -> typing.List[int]:
    ifact = list(range(1, n + 1))
    ifact[-1] = pow(factorial(p, n)[-1], -1, p)
    return cumprod(p, ifact[::-1])[::-1]


def make_choose(
    p: int,
    n: int,
) -> typing.Callable[[int, int], int]:
    fact = factorial(p, n)
    ifact = factorial_inverse(p, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k: return 0
        return fact[n] * ifact[n - k] % p * ifact[k] % p

    return choose



def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    MOD = 10 ** 9 + 7
    choose = make_choose(MOD, 1 << 17)

    a.sort()

    s = 0
    for i, x in enumerate(a):
        ...
        s += x * choose(i, k - 1)
        s -= x * choose(n - i - 1, k - 1)
        s %= MOD
    print(s)

main()
