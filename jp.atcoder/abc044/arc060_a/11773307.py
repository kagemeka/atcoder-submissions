import sys
import numpy as np

n, a, *x = map(int, sys.stdin.read().split())

def main():
    m = 2500
    dp = np.zeros((n + 1, m + 1), dtype=np.int64)
    dp[0, 0] = 1
    for i in range(n):
        dp[1:, x[i]:] += dp[:-1, :-x[i]].copy()
    i = np.arange(1, n + 1)
    print(dp[i, i * a].sum())

if __name__ ==  '__main__':
    main()
