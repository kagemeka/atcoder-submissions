import sys
import numpy as np

MOD = 10 ** 9 + 7

def main():
    n, A, B, *a = map(int, sys.stdin.read().split())
    a = np.array(a, dtype=np.int64)
    a = np.sort(a)
    if A == 1:
        print(*a, sep='\n')
        sys.exit()

    b = np.ceil(np.log(np.full(n, a[-1]) / a) / np.log(A)).astype(np.int64)
    remainder = B - np.sum(b)
    if remainder > 0:
        a = np.sort(a * A ** b)
        q, r = divmod(remainder, n)
        a = a * pow(A, int(q), MOD) % MOD
        a[:r] *= A
        a[:r] %= MOD
        print(*a[r:], sep='\n')
        print(*a[:r], sep='\n')
    else:
        for _ in range(B):
            a[0] *= A
            a = np.sort(a)
        ans = a % MOD
        print(*ans, sep='\n')


if __name__ == '__main__':
    main()
