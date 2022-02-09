import typing
import sys
import numpy as np

def main() -> typing.NoReturn:
    s = int(input())
    c = [1, 0, 0]
    if s < 3:
        print(c[s])
        return
    c = np.array(c)
    a = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
    ])

    MOD = 10 ** 9 + 7
    k = s - 2
    b = np.identity(3, np.int64)
    while k:
        if k & 1:
            b = a.dot(b) % MOD
        a = a.dot(a) % MOD
        k >>= 1
    c = b.dot(c) % MOD
    print(c[-1])

main()
