import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(c: np.ndarray) -> typing.NoReturn:
    n = len(c)
    mod = 10 ** 9 + 7
    v = 1
    c.sort()
    for i in range(n):
        v *= max(0, c[i] - i)
        v %= mod
    print(v)


def main() -> typing.NoReturn:
    n = int(input())
    c = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(c)


main()
