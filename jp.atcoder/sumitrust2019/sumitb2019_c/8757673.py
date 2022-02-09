import sys
import numpy as np
def main():
    x = int(sys.stdin.readline().rstrip())

    if x < 100:
        print(0)
        sys.exit()
    if 100 <= x <= 105:
        print(1)
        sys.exit()

    dp = np.zeros_like(np.arange(x+1), dtype=bool)
    dp[100:106] = True
    for i in range(106, x+1):
        dp[i] =  np.any(dp[i-105:i-99])

    print(dp[x] & 1)

if __name__ == '__main__':
    main()
