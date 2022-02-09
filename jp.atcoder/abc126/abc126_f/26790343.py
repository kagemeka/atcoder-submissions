import typing
import sys
# import numpy as np
# import numba as nb


def main() -> typing.NoReturn:
    m, k = map(int, input().split())
    n = pow(2, m)
    if k >= n or m == k == 1:
        print(-1)
        return

    a = [-1] * (n << 1)
    ptr = 0
    for i in range(n):
        if i == k: continue
        a[ptr] = i
        ptr += 1
    a[ptr] = k
    ptr += 1
    for i in range(n - 1, -1, -1):
        if i == k: continue
        a[ptr] = i
        ptr += 1
    a[-1] = k
    print(*a)

main()
