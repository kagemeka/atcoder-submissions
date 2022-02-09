import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], ) * 3, cache=True)
def solve(a: np.ndarray, b: np.ndarray, p: np.ndarray) -> typing.NoReturn:
    n = len(a)
    c = np.empty(n, np.int64)
    for i in range(n): c[p[i]] = i
    k = 0
    res = []
    for i in np.argsort(a, kind='mergesort'):
        j = c[i]
        if j == i: continue
        if b[p[i]] >= a[i] or b[i] >= a[j]:
            print(-1)
            return
        k += 1
        p[i], p[j] = i, p[i]
        c[i], c[p[j]] = i, j
        res.append((i, j))
    print(k)
    for i, j in res:
        print(i + 1, j + 1)



def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    b = np.array(sys.stdin.readline().split(), dtype=np.int64)
    p = np.array(sys.stdin.readline().split(), dtype=np.int64) - 1
    solve(a, b, p)


main()
