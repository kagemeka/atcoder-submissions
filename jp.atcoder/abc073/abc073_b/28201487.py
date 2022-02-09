import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n = int(input())
    l, r = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2).T

    print(np.sum(r - l + 1))

main()
