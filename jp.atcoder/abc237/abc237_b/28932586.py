import typing
import numpy as np
import sys


def main() -> None:
    h, w = map(int, input().split())
    a = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(h, w)
    a = a.T
    for row in a.tolist():
        print(*row)


if __name__ == "__main__":
    main()
