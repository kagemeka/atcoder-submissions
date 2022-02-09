import typing
import numpy as np
import sys


import numba as nb



@nb.njit((nb.i8[:, :], nb.i8, nb.i8[:], nb.i8[:, :]), cache=True)
def solve(xy: np.ndarray, m: int, op: np.ndarray, query: np.ndarray) -> typing.NoReturn:
    n = len(xy)
    q = len(query)
    a = np.zeros((m + 1, 3, 3), np.int64)
    a[0] = np.identity(3, np.int64)
    for i in range(m):
        if op[0] == 1:
            a[i + 1] = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
            op = op[1:]
        elif op[0] == 2:
            a[i + 1] = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
            op = op[1:]
        elif op[0] == 3:
            a[i + 1] = np.array([[-1, 0, 2 * op[1]], [0, 1, 0], [0, 0, 1]])
            op = op[2:]
        elif op[0] == 4:
            a[i + 1] = np.array([[1, 0, 0], [0, -1, 2 * op[1]], [0, 0, 1]])
            op = op[2:]
    for i in range(m):
        cum = np.zeros((3, 3), np.int64)
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    cum[j, k] += a[i + 1, j, l] * a[i, l, k]
        a[i + 1] = cum

    for i in range(q):
        b, c = query[i]
        c -= 1
        x, y = xy[c]
        arr = np.array([x, y, 1])
        x = np.sum(a[b, 0] * arr)
        y = np.sum(a[b, 1] * arr)
        print(x, y)


def main() -> typing.NoReturn:
    I = np.array(sys.stdin.read().split(), dtype=np.int64)
    n = I[0]
    I = I[1:]
    xy = I[:2 * n].reshape(n, 2)
    I = I[2 * n:]
    m = I[0]
    I = I[1:]
    cnt = 0
    i = 0
    while cnt < m:
        if I[i] == 1 or I[i] == 2:
            i += 1
        elif I[i] == 3 or I[i] == 4:
            i += 2
        cnt += 1
    op = I[:i]
    I = I[i:]
    q = I[0]
    I = I[1:]
    query = I[:q * 2].reshape(q, 2)
    solve(xy, m, op, query)


main()
