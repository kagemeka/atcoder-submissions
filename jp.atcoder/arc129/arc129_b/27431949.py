import typing
# import bisect
import numpy as np
import numba as nb
import sys



@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, lr: np.ndarray) -> typing.NoReturn:
    l, r = lr[:, 0], lr[:, 1]
    for i in range(n - 1):
        l[i + 1] = max(l[i], l[i + 1])
        r[i + 1] = min(r[i], r[i + 1])
    res = np.zeros(n, np.int64)
    for i in range(n):
        if l[i] <= r[i]: continue
        res[i] = (l[i] - r[i] + 1) // 2
    for x in res:
        print(x)



def main() -> typing.NoReturn:
    n = int(input())
    lr = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(n, lr)


main()
