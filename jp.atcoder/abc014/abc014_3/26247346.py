import sys
import typing

import numba as nb
import numpy as np


def solve(ab: np.ndarray) -> typing.NoReturn:
    m = 1 << 20
    c = np.zeros(m, np.int64)
    a, b = ab.T
    np.add.at(c, a, 1)
    np.add.at(c, b + 1, -1)
    np.cumsum(c, out=c)
    print(c.max())


def main() -> typing.NoReturn:
    n = int(input())
    ab = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(ab)


main()
