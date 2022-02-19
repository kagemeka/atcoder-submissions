import sys
import typing

import numba as nb
import numpy as np


@nb.njit((nb.i8,) * 6 + (nb.i8[:, :],), cache=True)
def solve(
    sx: int,
    sy: int,
    gx: int,
    gy: int,
    t: int,
    v: int,
    xy: np.ndarray,
) -> typing.NoReturn:
    for i in range(len(xy)):
        x, y = xy[i]
        d0 = np.sqrt((x - sx) ** 2 + (y - sy) ** 2)
        d1 = np.sqrt((gx - x) ** 2 + (gy - y) ** 2)
        if d0 + d1 <= v * t:
            print("YES")
            return
    print("NO")


def main() -> typing.NoReturn:
    sx, sy, gx, gy, t, v = map(int, input().split())
    n = int(input())
    xy = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(sx, sy, gx, gy, t, v, xy)


main()
