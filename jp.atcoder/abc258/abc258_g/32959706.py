# mypy: ignore-errors
import typing


M0 = 0x5555555555555555
M1 = 0x3333333333333333
M2 = 0x0F0F0F0F0F0F0F0F


def popcount(n: int) -> int:
    n -= (n >> 1) & M0
    n = (n & M1) + ((n >> 2) & M1)
    n = (n + (n >> 4)) & M2
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x7F


import numpy as np

N = 63


def new(size: int) -> np.ndarray:
    return np.zeros((size + N - 1) // N, np.int64)


def get(a: np.ndarray, i: np.ndarray) -> np.ndarray:
    return a[i // N] >> (i % N) & 1


def set(a: np.ndarray, i: np.ndarray, value: np.ndarray) -> None:
    flip(a, i[get(a, i) != value])


def flip(a: np.ndarray, i: np.ndarray) -> None:
    np.bitwise_xor.at(a, i // N, 1 << i % N)


def bit_and(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = min(a.size, b.size)
    a[:n] &= b[:n]
    return a


def main() -> None:
    n = int(input())

    m = (n + N - 1) // N
    a = np.zeros((n, m), np.int64)

    for i in range(n):
        set(a[i], np.arange(n), np.array(list(map(int, input()))))

    cnt = 0
    for i in range(n):
        j = np.arange(i)
        j = j[get(a[i], j) == 1]
        cnt += popcount((a[i] & a[j])).sum()
    print(cnt // 3)


main()
