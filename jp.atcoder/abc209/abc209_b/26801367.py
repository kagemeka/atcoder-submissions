import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    s = a.sum() - n // 2
    print('Yes' if x >= s else 'No')

main()
