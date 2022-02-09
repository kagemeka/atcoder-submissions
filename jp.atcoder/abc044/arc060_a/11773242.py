import sys
import numpy as np

n, a, *x = map(int, sys.stdin.read().split())

def main():
    m = 2500
    dp = np.zeros((n + 1, m + 1), dtype=np.int64)
    dp[0, 0] = 1
    for i in range(n):
        ndp = np.copy(dp)
        ndp[1:, x[i]:] += dp[:-1, :m-x[i]+1]
        dp = ndp
    i = np.arange(1, n + 1)
    print(np.sum(dp[i, i * a]))

if __name__ ==  '__main__':
    main()
