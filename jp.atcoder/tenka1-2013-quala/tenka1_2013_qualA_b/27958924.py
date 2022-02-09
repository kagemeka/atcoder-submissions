import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 5).sum(axis=1)
    print(np.sum(a < 20))

main()
