import sys
import numpy as np
from math import log, ceil
MOD = 10 ** 9 + 7

def main():
    n, A, B, *a = map(int, sys.stdin.read().split())
    a = np.array(a, dtype=np.int64)
    a = np.sort(a)
    if A == 1:
        print('\n'.join(map(str, a)))
        sys.exit()

    b = np.full(n, a[-1])
    b = np.ceil(np.log(b / a) / log(A)).astype(np.int64)

    remainder = B - np.sum(b)
    if remainder >= 0:
        a = np.sort(a * A ** b)
        q, r = divmod(remainder, n)
        a[:r] *= A
        a = np.sort(a) % MOD
        res = np.full(n, 1)
        res *= pow(A, int(q), MOD)
        ans = a * res % MOD
    else:
        # 2^30 > 10 ** 9, n <= 50より, B < 1500なので毎回sortで十分間に合う。
        for _ in range(B):
            a[0] *= A
            a = a.sort(a)
        ans = a % MOD

    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
