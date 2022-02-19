import sys
import typing

import numpy as np


def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    x = int(round(a.sum() / n))
    print(np.sum((x - a) ** 2))

main()
