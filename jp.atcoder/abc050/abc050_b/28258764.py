import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n = int(input())
    t = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    m = int(input())
    p, x = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(m, 2).T
    p -= 1

    s = t.sum()
    res = s + x - t[p]
    for i in res.tolist():
        print(i)


main()
