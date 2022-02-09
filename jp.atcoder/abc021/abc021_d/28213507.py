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
    mod: int,
    n: int,
) -> typing.Callable[[int, int], int]:
    fact = factorial(mod, n)
    ifact = factorial_inverse(mod, n)

    def choose(n: int, k: int) -> int:
        nonlocal fact, ifact
        if k < 0 or n < k: return 0
        return fact[n] * ifact[n - k] % mod * ifact[k] % mod

    return choose


def main() -> typing.NoReturn:
    n = int(input())
    k = int(input())
    # nHk = (n + k - 1)Ck
    MOD = 10 ** 9 + 7
    choose = make_choose(MOD, 1 << 20)
    print(choose(n + k - 1, k))

main()
