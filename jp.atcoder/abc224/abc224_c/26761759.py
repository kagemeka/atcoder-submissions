import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
    n = len(xy)
    cnt = 0
    for i in range(n - 2):
        x1, y1 = xy[i]
        for j in range(i + 1, n - 1):
            if j == i: continue
            x2, y2 = xy[j]
            for k in range(j + 1, n):
                if k == j: continue
                x3, y3 = xy[k]
                cnt += (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)
    print(cnt)




def main() -> typing.NoReturn:
    n = int(input())
    xy = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(xy)


main()
