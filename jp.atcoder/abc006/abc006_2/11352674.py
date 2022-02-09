import sys
import numpy as np

MOD = 10 ** 4 + 7

def matrix_pow_mod(x, n, mod):
    if n == 0:
        return np.identity(3)
    elif n == 1:
        return x

    y = x.dot(x) % mod
    res = np.identity(3)
    for i in range(21):
        if n >> i & 1:
            if i == 0:
                res = res.dot(x)
            else:
                res = res.dot(matrix_pow_mod(y, i, mod))
            res %= mod

    return res % mod

n = int(sys.stdin.readline().rstrip())

def main():
    A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    res = matrix_pow_mod(A, n, MOD).dot(np.array([0, 0, 1]))
    print(int(res[-1]))

if __name__ == '__main__':
    main()
