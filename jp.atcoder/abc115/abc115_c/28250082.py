import typing
import sys
import numpy as np



def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    h = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    )
    h.sort()
    print(np.min(h[k - 1:] - h[:-(k - 1)]))

main()
