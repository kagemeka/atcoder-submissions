import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(v: np.ndarray, k: int) -> typing.NoReturn:
    n = len(v)
    mx = 0
    for i in range(min(k, n) + 1):
        for j in range(i + 1):
            a = np.hstack((v[:j], v[n - i + j:]))
            a.sort()
            s = a.sum()
            for j in range(k - i):
                if j >= len(a) or a[j] >= 0: break
                s -= a[j]
            mx = max(mx, s)
    print(mx)



def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    v = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    solve(v, k)


main()
