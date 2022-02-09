import typing
import sys
import numpy as np

def main() -> typing.NoReturn:
    n = int(input())
    a, b = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 2).T
    print(np.sum((a + b) * (b - a + 1) // 2))

main()
