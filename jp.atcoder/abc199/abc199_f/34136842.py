# mypy: ignore-errors

import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.readline


def mul(mod: int, a: np.ndarray, b: np.ndarray) -> np.ndarray:
    B = 16
    MASK = (1 << B) - 1
    assert np.ndim(a) == np.ndim(b) == 2 and a.shape[1] == b.shape[0]
    assert 0 < mod < 1 << (1 << B)
    a %= mod
    b %= mod
    a0, a1, b0, b1 = a & MASK, a >> B, b & MASK, b >> B
    c0 = np.dot(a0, b0) % mod
    c2 = np.dot(a1, b1) % mod
    c1 = np.dot(a0 + a1, b0 + b1) - c0 - c2
    c1 %= mod
    c = (c2 << (B << 1)) + (c1 << B) + c0
    return c % mod


def power(mod: int, a: np.ndarray, n: int) -> np.ndarray:
    if n == 0:
        m = len(a)
        return np.eye(m, dtype=np.int64)
    y = power(mod, a, n >> 1)
    y = mul(mod, y, y)
    if n & 1:
        y = mul(mod, y, a)
    return y


def main() -> None:
    n, m, k = map(int, readline().split())
    mod = 1_000_000_007
    d = pow(2 * m, -1, mod)
    a = np.array(readline().split(), dtype=np.int64)[:, None]
    b = np.eye(n, dtype=np.int64)
    u, v = np.array(read().split(), dtype=np.int64).reshape(m, 2).T - 1
    np.add.at(b, (u, u), -d)
    np.add.at(b, (u, v), d)
    np.add.at(b, (v, v), -d)
    np.add.at(b, (v, u), d)
    b %= mod
    b = power(mod, b, k)
    a = mul(mod, b, a).ravel()
    print(*a, sep="\n")


if __name__ == "__main__":
    main()
