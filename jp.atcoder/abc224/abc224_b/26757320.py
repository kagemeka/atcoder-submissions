import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    h, w = a.shape
    for i1 in range(h - 1):
        for j1 in range(w - 1):
            for i2 in range(i1 + 1, h):
                for j2 in range(j1 + 1, w):
                    if a[i1, j1] + a[i2, j2] <= a[i2, j1] + a[i1, j2]: continue
                    print('No')
                    return
    print('Yes')


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    a = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(h, w)
    solve(a)


main()
