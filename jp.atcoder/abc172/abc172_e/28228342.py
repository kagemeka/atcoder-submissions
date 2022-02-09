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


def make_choose(p: int, n: int) -> typing.Callable[[int, int], int]:
    fact = factorial(p, n)
    ifact = factorial_inverse(p, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k: return 0
        return fact[n] * ifact[n - k] % p * ifact[k] % p

    return choose



def main() -> typing.NoReturn:
    n, m = map(int, input().split())

    # inclusion exclusion principle

    MOD = 10 ** 9 + 7

    choose = make_choose(MOD, 1 << 20)
    fact = factorial(MOD, 1 << 20)

    def p(n: int, k: int) -> int:
        return choose(n, k) * fact[k] % MOD

    s = 0
    sign = 1
    for k in range(n + 1):
        s += choose(m, k) * p(n, k) % MOD * (p(m - k, n - k) ** 2 % MOD) % MOD * sign
        s %= MOD
        sign *= -1
    print(s)


main()
