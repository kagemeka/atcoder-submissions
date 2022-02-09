import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(xy: np.ndarray) -> typing.NoReturn:
    n = len(xy)
    inf = 1 << 60
    l = np.empty(n, np.float64)
    r = np.empty(n, np.float64)
    for i in range(n):
        x, y = xy[i]
        # l[i] = (y - 1) / x
        l[i] = np.arctan2(y - 1, x)
        # r[i] = inf if x == 1 else y / (x - 1)
        r[i] = np.arctan2(y, x - 1)
    v = np.unique(np.hstack((l, r)))
    ri = np.searchsorted(v, r)
    li = np.searchsorted(v, l)
    sort_idx = np.argsort(ri, kind='mergesort')
    li = li[sort_idx]
    ri = ri[sort_idx]
    c = t = 0
    for i in range(n):
        a, b = li[i], ri[i]
        if a < t: continue
        c += 1
        t = b
    print(c)



def main() -> typing.NoReturn:
    n = int(input())
    xy = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(xy)


main()
