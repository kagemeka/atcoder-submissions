import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def pow_(mod: int, x: int, n: int) -> int:
    y = 1
    while n:
        if n & 1: y = y * x % mod
        x = x * x % mod
        n >>= 1
    return y


@nb.njit((nb.i8, ), cache=True)
def solve(l: int) -> typing.NoReturn:
    mod = 10 ** 9 + 7
    m = 10 << 17
    f = np.zeros(m, np.int64)
    g = np.zeros(m, np.int64)
    h = np.zeros(m, np.int64)
    f[0] = 1
    g[0] = 2
    h[0] = 1
    for i in range(m - 1):
        f[i + 1] = (3 * f[i] + pow_(mod, g[i], 3)) % mod
        x = (g[i] * g[i] - h[i] * h[i]) % mod
        g[i + 1] = (x + g[i]) * g[i] % mod
        h[i + 1] = x * h[i] % mod
    print(f[l])



def main() -> typing.NoReturn:
    l = int(input())
    solve(l)


main()
