import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(dc: np.ndarray) -> typing.NoReturn:
    m = len(dc)
    d, c = dc[:, 0], dc[:, 1]
    s = np.sum(d * c)
    l = c.sum()
    a = l * 9 + s
    q, r = divmod(a, 9)
    q -= 1
    print(q)



def main() -> typing.NoReturn:
    m = int(input())
    dc = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(m, 2)
    solve(dc)


main()
