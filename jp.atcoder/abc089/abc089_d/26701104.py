import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], nb.i8, nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, d: int, lr: np.ndarray) -> typing.NoReturn:
    h, w = a.shape
    coord = np.empty((h * w, 2), np.int64)
    for i in range(h):
        for j in range(w):
            coord[a[i, j]] = (i, j)

    cost = np.zeros(h * w, np.int64)
    for k in range(d):
        while k + d < h * w:
            cost[k + d] = cost[k] + np.abs(coord[k + d] - coord[k]).sum()
            k += d
    for i in range(len(lr)):
        l, r = lr[i]
        print(cost[r] - cost[l])


def main() -> typing.NoReturn:
    h, w, d = map(int, input().split())
    I = np.array(sys.stdin.read().split(),dtype=np.int64)
    a = I[:h * w].reshape(h, w) - 1
    lr = I[h * w + 1:].reshape(-1, 2) - 1
    solve(a, d, lr)


main()
