import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
    n = len(a)
    que = np.argsort(a, kind='mergesort')[::-1]
    b = np.empty(n, np.int64)
    b[0] = 0
    ptr = 1
    for i in range(1, n):
        if a[i] <= a[b[ptr - 1]]: continue
        b[ptr] = i
        ptr += 1
    b = b[:ptr]

    h = 1 << 60
    ptr -= 1
    idx = -1
    cnt = np.zeros(n + 1, np.int64)
    for i in range(n):
        j = que[i]
        cnt[idx] += (h - a[j]) * i
        h = a[j]
        if j == b[ptr]:
            idx = j
            ptr -= 1
        if idx == 0: break
    cnt[0] = a.sum() - cnt.sum()
    for x in cnt[:-1]:
        print(x)

def main() -> typing.NoReturn:
    n = int(input())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    res = solve(a)


main()
