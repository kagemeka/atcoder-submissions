import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8, nb.i8, nb.i8), cache=True)
def solve(a: np.ndarray, m: int, v: int, p: int) -> typing.NoReturn:
    n = len(a)
    a.sort()


    def possible(i):
        j = np.searchsorted(a, a[i] + m, side='right')
        if n - j >= p: return False
        k = np.searchsorted(a, a[i], side='right')
        if k + p - 1 >= v: return True
        s = 0
        for j in range(k, n - p + 1):
            s += a[i] + m - a[j]
        return s >= (v - k - p + 1) * m


    def binary_search():
        lo, hi = -1, n - 1
        while hi - lo > 1:
            i = (lo + hi) >> 1
            if possible(i):
                hi = i
            else:
                lo = i
        return hi
    print(n - binary_search())


def main() -> typing.NoReturn:
    n, m, v, p = map(int, input().split())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a, m, v, p)


main()
