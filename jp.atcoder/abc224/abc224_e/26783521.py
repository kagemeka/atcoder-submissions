import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(h: int, w: int, rca: np.ndarray) -> typing.NoReturn:
    n = len(rca)

    dist = np.zeros(n, np.int64)
    rmax = np.full(h, -1, np.int64)
    cmax = np.full(w, -1, np.int64)

    order = np.argsort(rca[:, 2], kind='mergesort')[::-1]

    s = 0
    prev = -1
    for i in range(n):
        if rca[order[i], 2] != prev:
            for j in range(s, i):
                r, c, a = rca[order[j]]
                rmax[r] = max(rmax[r], dist[order[j]])
                cmax[c] = max(cmax[c], dist[order[j]])
            s = i
        r, c, a = rca[order[i]]
        dist[order[i]] = max(rmax[r], cmax[c]) + 1
        prev = a

    for d in dist:
        print(d)


def main() -> typing.NoReturn:
    h, w, n = map(int, input().split())
    rca = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 3)
    rca[:, :2] -= 1
    solve(h, w, rca)


main()
