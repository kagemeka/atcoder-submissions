# mypy: ignore-errors

import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.readline

fft = np.fft.rfft
ifft = np.fft.irfft


def main() -> None:
    n = int(readline())
    a, b = np.pad(
        np.array(read().split(), np.int64).reshape(-1, 2), ((1, 0), (0, 0))
    ).T
    m = 1 << n.bit_length() + 2
    a = np.rint(ifft(fft(a, m) * fft(b, m), m)).astype(np.int64)
    print("\n".join(map(str, a[1 : (n << 1) + 1].tolist())))


if __name__ == "__main__":
    main()
