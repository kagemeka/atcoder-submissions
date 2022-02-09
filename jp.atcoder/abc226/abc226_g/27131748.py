import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, b: np.ndarray) -> typing.NoReturn:
    n = 5
    for i in range(n - 1, -1, -1):
        x = min(a[i], b[i])
        b[i] -= x
        a[i] -= x
        if b[i] > 0: continue
        ok = False
        for j in range(n - 1, i, -1):
            q, r = divmod(j + 1, i + 1)
            c, r2 = divmod(a[i], q)
            if c <= b[j]:
                b[j] -= c
                a[i] -= c * q
                if r >= 1: b[r - 1] += c
                if b[j] > 0:
                    b[j] -= 1
                    assert j >= j + 1 - (i + 1) * r2 - 1 >= 0
                    b[j + 1 - (i + 1) * r2 - 1] += 1
                    a[i] = 0
                    break
            else:
                a[i] -= q * b[j]
                if r >= 1: b[r - 1] += b[j]
                b[j] = 0
        if a[i] == 0: ok = True
        if ok: continue
        print('No')
        return
    print('Yes')


def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        a = np.array(sys.stdin.readline().split(), dtype=np.int64)
        b = np.array(sys.stdin.readline().split(), dtype=np.int64)
        solve(a, b)



main()
