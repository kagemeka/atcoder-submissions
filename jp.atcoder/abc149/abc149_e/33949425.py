# mypy: ignore-errors

import sys
import numpy as np


def main() -> None:
    n, m, *a = map(int, sys.stdin.read().split())
    a = np.array(a)
    k = 1 << 18
    c = np.zeros(k)
    np.add.at(c, a, 1)
    fft = np.fft.rfft
    ifft = np.fft.irfft
    c = fft(c, k)
    c = np.rint(ifft(c * c, k)).astype(np.int64)
    s = (c * np.arange(k))[::-1].cumsum()
    c = c[::-1].cumsum()
    i = np.searchsorted(c, m)
    res = (k - 1 - i) * (m - c[i - 1]) + s[i - 1]
    print(res)


main()
