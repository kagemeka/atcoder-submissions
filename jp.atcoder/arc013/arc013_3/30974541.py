import sys
import numpy as np


def main() -> None:
    # nim of nim
    n = int(input())
    grundy_numbers = []
    for _ in range(n):
        xyz = np.array(sys.stdin.readline().split(), dtype=np.int64)
        m = int(input())
        a = np.array(
            [sys.stdin.readline().split() for _ in range(m)],
            dtype=np.int64,
        )
        grundy_numbers.append(
            np.bitwise_xor.reduce(a.min(axis=0))
            ^ np.bitwise_xor.reduce(
                xyz - a.max(axis=0) - 1,
            )
        )
    grundy_nim = 0
    for g in grundy_numbers:
        grundy_nim ^= g
    print("WIN" if grundy_nim else "LOSE")


if __name__ == "__main__":
    main()
