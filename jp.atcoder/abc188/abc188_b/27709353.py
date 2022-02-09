import typing
import numpy as np
import sys


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    b = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    print('Yes' if a.dot(b) == 0 else 'No')


main()
