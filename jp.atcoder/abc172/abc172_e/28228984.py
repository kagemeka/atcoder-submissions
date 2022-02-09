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
    ifact[-1] = pow(factorial(p, n)[-1], p - 2, p)
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
    # \sum_{k=0}^{n}{mPn * nCk * (m - k)P(n - k)}
    # = mPn * \sum_{k=0}^{n}{nCk * (m - k)P(n - k)}
    # mPn := patterns of A
    # nCk := there are k indices out of n such that A_i = B_i.
    # (m - k)P(n - k) := patterns of B (A_i \neq B_i)
    for k in range(n + 1):
        # complete permutation
        s += choose(n, k) * p(m - k, n - k) % MOD * sign
        s %= MOD
        sign *= -1
    s *= p(m, n)
    s %= MOD
    print(s)


main()
