import sys
import numpy as np

MOD = 10 ** 4 + 7

def Tribonacci(n):
    A = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0]])
    B = A.copy()
    for _ in range(n-2):
        B = np.dot(B, A) % MOD
    return B[2][0]

n = int(sys.stdin.readline().rstrip())

def main():
    print(Tribonacci(n))

if __name__ == '__main__':
    main()
