import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def gpf(n: int) -> np.ndarray:
    a = np.arange(n)
    a[:2] = -1
    i = 0
    while i * i < n - 1:
        i += 1
        if a[i] == i: a[i::i] = i
    return a


@nb.njit
def prime_factorize_gpf(n: int, gpf: np.ndarray) -> np.ndarray:
    prime, cnt = [-1], [-1]
    while n > 1:
        p = gpf[n]
        n //= p
        if prime[-1] == p:
            cnt[-1] += 1
            continue
        prime.append(p)
        cnt.append(1)
    return np.vstack((np.array(prime), np.array(cnt))).T[1:]


@nb.njit
def pow_recurse(mod: int, x: int, n: int) -> int:
    if n == 0: return 1
    y = pow_recurse(mod, x, n >> 1)
    y = y * y % mod
    if n & 1: y = y * x % mod
    return y


@nb.njit
def cumprod(mod: int, a: np.ndarray) -> typing.NoReturn:
    for i in range(len(a) - 1): a[i + 1] = a[i + 1] * a[i] % mod

@nb.njit
def factorial(mod: int, n: int) -> np.ndarray:
    a = np.arange(n)
    a[0] = 1
    cumprod(mod, a)
    return a

@nb.njit
def inverse_fermat(p: int, n: int) -> int:
    return pow_recurse(p, n, p - 2)

@nb.njit
def factorial_inverse(p: int, n: int) -> np.ndarray:
    a = np.arange(1, n + 1)
    a[-1] = inverse_fermat(p, factorial(p, n)[-1])
    cumprod(p, a[::-1])
    return a


@nb.njit
def inverse_table(mod: int, n: int) -> np.ndarray:
    a = factorial_inverse(mod, n)
    a[1:] *= factorial(mod, n - 1)
    return a


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    mod = 10 ** 9 + 7
    n = len(a)
    m = 1 << 20
    g = gpf(m)
    b = np.zeros(m, np.int64)
    for x in a:
        for p, c in prime_factorize_gpf(x, g):
            b[p] = max(b[p], c)

    l = 1
    for i in np.flatnonzero(b):
        l = l * pow_recurse(mod, i, b[i]) % mod

    inv = inverse_table(mod, m)
    s = inv[a].sum() % mod
    print(l * s % mod)


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a)


main()
