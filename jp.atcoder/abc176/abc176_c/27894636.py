import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    b = np.maximum.accumulate(a)
    print(np.sum(b - a))


main()
