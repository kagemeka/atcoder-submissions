import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    n = len(a)

    s = 1000
    cnt = 0
    for i in range(n - 1):
        s += a[i] * cnt
        cnt = 0
        if a[i + 1] <= a[i]: continue
        cnt, s = divmod(s, a[i])
    s += a[-1] * cnt
    print(s)


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a)


main()
