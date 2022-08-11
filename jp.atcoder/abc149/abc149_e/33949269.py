# mypy: ignore-errors

from scipy.signal import convolve
import sys
import numpy as np


def main() -> None:
    n, m, *a = map(int, sys.stdin.read().split())
    a = np.array(a)
    k = 1 << 17
    c = np.bincount(a)
    c = np.rint(convolve(c, c)).astype(np.int64)

    k = c.size
    s = (c * np.arange(k))[::-1].cumsum()
    c = c[::-1].cumsum()
    i = np.searchsorted(c, m)
    res = (k - 1 - i) * (m - c[i - 1]) + s[i - 1]
    print(res)


main()
