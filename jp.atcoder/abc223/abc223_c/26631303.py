import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
    n = len(ab)
    a = ab[:, 0]
    b = ab[:, 1]
    t0 = np.sum(a / b) / 2
    x = 0
    t = 0
    for i in range(n):
        if t + a[i] / b[i] <= t0:
            t += a[i] / b[i]
            x += a[i]
            continue
        x += b[i] * (t0 - t)
        break
    print(x)



def main() -> typing.NoReturn:
    n = int(input())
    ab = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2)
    solve(ab)


main()
