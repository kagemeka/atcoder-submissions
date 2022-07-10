# mypy: ignore-errors
import numpy as np


def main() -> None:
    n = int(input())
    a = np.array(list(map(int, input().split())))
    k = 60
    b = a[:, None] >> np.arange(k) & 1
    b = b.sum(axis=0)
    MOD = 10**9 + 7
    res = np.sum(b * (n - b) % MOD * ((1 << np.arange(k)) % MOD) % MOD) % MOD
    print(res)


main()
