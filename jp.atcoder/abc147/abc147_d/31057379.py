import numpy as np
import sys


def main() -> None:
    MOD = 10**9 + 7
    n = int(sys.stdin.readline().rstrip())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    K = 60

    c = (a[:, None] >> np.arange(K) & 1).sum(axis=0)
    res = np.sum(c * (n - c) % MOD * ((1 << np.arange(K)) % MOD) % MOD) % MOD
    print(res)


if __name__ == "__main__":
    main()
