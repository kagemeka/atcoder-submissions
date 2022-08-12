# mypy: ignore-errors

import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.readline


def convolve(a: np.ndarray, b: np.ndarray, n: int = 1 << 18) -> np.ndarray:
    return np.rint(
        np.fft.irfft(np.fft.rfft(a, n) * np.fft.rfft(b, n), n),
    ).astype(np.int64)


def main() -> None:
    n, m, *a = map(int, read().split())
    a = np.array(a)
    k = 1 << 18
    c = np.bincount(a)
    c = convolve(c, c, k)
    s = (c * np.arange(k))[::-1].cumsum()
    c = c[::-1].cumsum()
    i = np.searchsorted(c, m)
    res = (k - 1 - i) * (m - c[i - 1]) + s[i - 1]
    print(res)


if __name__ == "__main__":
    main()
