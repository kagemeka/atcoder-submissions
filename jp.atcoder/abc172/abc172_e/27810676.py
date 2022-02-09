import typing




def cumprod(mod: int, a: list[int]) -> typing.NoReturn:
    """Compute cumprod over modular in place.

    the parameter a must be one dimentional list.
    """
    for i in range(len(a) - 1): a[i + 1] = a[i + 1] * a[i] % mod

def inverse(mod: int, n: int) -> int: return pow(n, -1, mod)

def factorial(mod: int, n: int) -> list[int]:
    a = list(range(n))
    a[0] = 1
    cumprod(mod, a)
    return a

def factorial_inverse(p: int, n: int) -> list[int]:
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

    choose = Choose(MOD, 1 << 20)
    permutate = CountPermutation(MOD, 1 << 20)
    cnt = 0
    sign = 1
    for k in range(n + 1):
        cnt += permutate(m - k, n - k) * choose(n, k) % MOD * sign
        sign *= -1
    cnt %= MOD
    cnt *= permutate(m, n)
    cnt %= MOD
    print(cnt)




class Choose():
    def __call__(self, n: int, k: int) -> int:
        p, fact, ifact = self.__p, self.__fact, self.__ifact
        ok = 0 <= k <= n
        return fact[n] * ifact[n - k] % p * ifact[k] % p * ok

    def __init__(self, p: int, n: int) -> typing.NoReturn:
        self.__p = p
        self.__fact = factorial(p, n)
        self.__ifact = factorial_inverse(p, n)



class CountPermutation():
    def __call__(self, n: int, k: int) -> int:
        p, fact, ifact = self.__p, self.__fact, self.__ifact
        ok = 0 <= k <= n
        return fact[n] * ifact[n - k] % p * ok

    def __init__(self, p: int, n: int) -> typing.NoReturn:
        self.__p = p
        self.__fact = factorial(p, n)
        self.__ifact = factorial_inverse(p, n)



main()
