import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(ab: np.ndarray) -> typing.NoReturn:
    n = len(ab)
    c = np.bincount(ab.ravel())
    print('Yes' if np.any(c == n) else 'No')



def main() -> typing.NoReturn:
    n = int(input())
    ab = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n - 1, 2)
    solve(ab)


main()
