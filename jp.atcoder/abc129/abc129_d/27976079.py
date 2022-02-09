import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    s = np.array(
        [list(input()) for _ in range(h)],
        dtype='U1',
    )
    inf = 1 << 60
    a = np.where(s == '#', 0, inf)
    a = np.pad(a, 1)

    def count(a: np.ndarray) -> np.ndarray:
        n = len(a)
        for i in range(n - 1):
            np.minimum(a[i + 1], a[i] + 1, out=a[i + 1])
        return a

    u = count(a.copy())
    l = count(a.copy().T).T
    d = count(a.copy()[::-1])[::-1]
    r = count(a.copy().T[::-1])[::-1].T
    cnt = np.maximum(0, (u + l + d + r - 3))
    print(cnt.max())

main()
