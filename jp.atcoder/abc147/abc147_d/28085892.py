import typing
import sys
import numpy as np

def main() -> typing.NoReturn:
    # compute sum per digit

    n = int(input())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    k = 60
    MOD = 10 ** 9 + 7
    b = np.sum(a[:, None] >> np.arange(k) & 1, axis=0)
    s = np.sum((1 << np.arange(k)) % MOD * b % MOD * (n - b) % MOD) % MOD
    print(s)

main()
