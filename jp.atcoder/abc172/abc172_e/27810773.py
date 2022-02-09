import typing




def cumprod(mod: int, a: typing.List[int]) -> typing.NoReturn:
    """Compute cumprod over modular in place.

    the parameter a must be one dimentional list.
    """
    for i in range(len(a) - 1): a[i + 1] = a[i + 1] * a[i] % mod

def inverse(mod: int, n: int) -> int: return pow(n, -1, mod)

def factorial(mod: int, n: int) -> typing.List[int]:
    a = list(range(n))
    a[0] = 1
    cumprod(mod, a)
    return a

def factorial_inverse(p: int, n: int) -> typing.List[int]:
    a = list(range(1, n + 1))
    a[-1] = inverse(p, factorial(p, n)[-1])
    a.reverse()
    cumprod(p, a)
    return a[::-1]

def main() -> typing.NoReturn:
    '''
    inclusion exclision principle
    '''
    MOD = 10 ** 9 + 7

    n, m = map(int, input().split())
    mx = 5 * 10 ** 5 + 1

    fact = factorial(MOD, mx)
    ifact = factorial_inverse(MOD, mx)
    def permutate(n: int, k: int) -> int:
        return fact[n] * ifact[n - k] % MOD

    def choose(n: int, k: int) -> int:
        return permutate(n, k) * ifact[k] % MOD

    cnt = 0
    sign = 1
    for k in range(n + 1):
        cnt += permutate(m - k, n - k) * choose(n, k) % MOD * sign
        sign *= -1
    cnt %= MOD
    cnt *= permutate(m, n)
    cnt %= MOD
    print(cnt)



main()
