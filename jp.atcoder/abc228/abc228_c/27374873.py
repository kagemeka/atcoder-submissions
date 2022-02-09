import typing
import numpy as np
import sys


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    p = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(n, 3)
    score = p.sum(axis=1)
    idx = score.argsort()
    possible = np.zeros(n, np.bool8)
    possible = score + 300 >= score[idx[-k]]
    for p in possible.tolist():
        print('Yes' if p else 'No')


main()
