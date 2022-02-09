import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def pow(mod: int, x: int, n: int) -> int:
    y = 1
    while n:
        if n & 1: y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


@nb.njit((nb.i8[:],), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    mod = 998_244_353
    n = len(a)
    a = a[::-1]
    s = a.cumsum()
    coeff = pow(mod, 2, n - 1)
    inv2 = pow(mod, 2, mod - 2)
    tot = 0
    d = 1
    for i in range(n):
        tot += coeff * d % mod * (a[i] + inv2 * (s[-1] - s[i]) % mod)
        tot %= mod
        coeff = coeff * inv2 % mod
        d = d * 10 % mod
    print(tot)


def main() -> typing.NoReturn:
    a = np.array(list(input()), dtype=np.int64)
    solve(a)


main()
