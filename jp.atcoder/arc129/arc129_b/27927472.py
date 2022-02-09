import typing
import numpy as np
import sys

def main() -> typing.NoReturn:
    n = int(input())
    l, r = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2).T
    l = np.maximum.accumulate(l)
    r = np.minimum.accumulate(r)
    res = np.maximum((l - r + 1) // 2, 0)
    for x in res.tolist():
        print(x)


main()
