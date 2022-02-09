import sys
import numpy as np

MOD = 10 ** 4 + 7

def tribonacci(n):
    A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    A = np.linalg.matrix_power(A, n-2)
    res = np.dot(A, np.array([1, 0, 0])) % MOD
    return res[0]

n = int(sys.stdin.readline().rstrip())

def main():
    print(tribonacci(n-1))

if __name__ == '__main__':
    main()
