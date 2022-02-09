import sys
import numpy as np

MOD = 10 ** 4 + 7

def matrix_power_mod(x, n, modulus):
    x = np.asanyarray(x)
    if len(x.shape) != 2:
        raise ValueError("input must be a matrix")
    if x.shape[0] != x.shape[1]:
        raise ValueError("input must be a square matrix")
    if not isinstance(n, int):
        raise ValueError("power must be an integer")

    if n < 0:
        x = np.linalg.inv(x)
        n = -n
    if n == 0:
        return np.identity(x.shape[0], dtype=x.dtype)
    y = None
    while n > 1:
        if n % 2 == 1:
            y = _matrix_mul_mod_opt(x, y, modulus=modulus)
        x = _matrix_mul_mod(x, x, modulus=modulus)
        n = n // 2
    return _matrix_mul_mod_opt(x, y, modulus=modulus)


def matrix_mul_mod(a, b, modulus):
    if len(a.shape) != 2:
        raise ValueError("input a must be a matrix")
    if len(b.shape) != 2:
        raise ValueError("input b must be a matrix")
    if a.shape[1] != a.shape[0]:
        raise ValueError("input a and b must have compatible shape for multiplication")
    return _matrix_mul_mod(a, b, modulus=modulus)


def _matrix_mul_mod_opt(a, b, modulus):
    if b is None:
        return a
    return _matrix_mul_mod(a, b, modulus=modulus)


def _matrix_mul_mod(a, b, modulus):
    r = np.zeros((a.shape[0], b.shape[1]), dtype=a.dtype)
    bT = b.T
    for rowindex in range(r.shape[0]):
        x = (a[rowindex, :] * bT) % modulus
        x = np.sum(x, 1) % modulus
        r[rowindex, :] = x
    return r

def tribonacci(n):
    A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    A = matrix_power_mod(A, n-2, MOD)
    res = np.dot(A, np.array([1, 0, 0])) % MOD
    return res[0]

n = int(sys.stdin.readline().rstrip())

def main():
    print(tribonacci(n-1))

if __name__ == '__main__':
    main()
