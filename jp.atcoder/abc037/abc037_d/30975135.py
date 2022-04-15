import sys
import numpy as np
import numba


@numba.njit(
    (
        numba.i8,
        numba.i8[:],
    ),
    cache=True,
)
def solve(h: int, a: np.ndarray) -> None:
    n = a.size
    w = n // h

    MOD = 10**9 + 7
    count = np.ones(n, dtype=np.int64)
    tot = 0
    for i in np.argsort(a):
        count[i] %= MOD
        tot += count[i]
        tot %= MOD
        y, x = divmod(i, w)
        if y < h - 1 and a[i + w] > a[i]:
            count[i + w] += count[i]
        if y > 0 and a[i - w] > a[i]:
            count[i - w] += count[i]
        if x < w - 1 and a[i + 1] > a[i]:
            count[i + 1] += count[i]
        if x > 0 and a[i - 1] > a[i]:
            count[i - 1] += count[i]
    print(tot)


def main() -> None:
    h, w, *a = map(int, sys.stdin.read().split())
    a = np.array(a)
    solve(h, a)


if __name__ == "__main__":
    main()
