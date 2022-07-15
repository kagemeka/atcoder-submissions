# mypy: ignore-errors
import numpy as np
import sys


def main() -> None:
    I = np.array(sys.stdin.read().split(), dtype=np.int64)
    n = I[0]
    t = I[1 : n + 1]
    m = I[n + 1]
    p, x = I[n + 2 :].reshape(m, 2).T
    res = t.sum() + x - t[p - 1]
    print(*res, sep="\n")


main()
