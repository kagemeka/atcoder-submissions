import sys
import numpy as np

inf = float('inf')

h, n, *ab = map(int, sys.stdin.read().split())
a, b = np.array(ab, dtype=np.int64).reshape(n, 2).T

def main():
    dp = np.zeros(h+1, dtype=np.int64)
    for i in range(1, h+1):
        dp[i] = np.amin(dp[np.maximum(i-a, 0)] + b)

    return dp[h]

if __name__ == '__main__':
    ans = main()
    print(ans)
