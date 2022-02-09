import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(b) -> typing.NoReturn:
    n, m = b.shape
    for i in range(n - 1):
        if not np.all(b[i + 1] == b[i] + 7):
            print('No')
            return
    for j in range(m - 1):
        if not np.all(b[:, j + 1] == b[:, j] + 1):
            print('No')
            return
    for i in range(7 - m + 1):
        if b[0, 0] % 7 == i + 1:
            print('Yes')
            return
    print('No')



def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    b = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, m)
    solve(b)



main()
