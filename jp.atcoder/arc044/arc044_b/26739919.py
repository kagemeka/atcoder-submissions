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


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    b = np.bincount(a)
    if b[0] != 1:
        print(0)
        return
    n = len(b)
    mod = 10 ** 9 + 7
    pow2 = np.ones(n, np.int64)
    for i in range(n - 1): pow2[i + 1] = pow2[i] * 2 % mod
    m = len(b)
    c = np.zeros(m, np.int64)
    c[0] = 1
    def choose2(n):
        return n * (n - 1) // 2

    for i in range(m - 1):
        c[i + 1] = c[i] * pow(mod, (pow2[b[i]] - 1) % mod, b[i + 1]) % mod * pow(mod, 2, choose2(b[i + 1])) % mod
    print(c[-1])



def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a)


main()
