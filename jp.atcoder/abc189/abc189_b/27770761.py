import typing
import sys
import numpy as np

def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    v, p = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2).T
    a = np.cumsum(v * p)
    x *= 100
    i = np.searchsorted(a, x, side='right')
    print(i + 1 if i < n else -1)


main()
