import sys
import typing

import numba as nb
import numpy as np


@nb.njit((nb.i8[:],), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    b = np.bincount(a)
    s = 0
    for x in b:
        s += max(0, x - 1)
    print(s)


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    )
    solve(a)


main()
