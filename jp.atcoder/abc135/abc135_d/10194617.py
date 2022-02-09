import sys
import numpy as np

MOD = 10 ** 9 + 7

s = sys.stdin.readline().rstrip()
l = len(s)

def main():
    dp = np.zeros(13, dtype=np.int64); dp[0] = 1
    for d in s:
        prev = dp.copy()
        dp = np.zeros(13, dtype=np.int64)
        if d != '?':
            d = int(d)
            np.add.at(dp, (np.arange(13)*10+d)%13, prev)
        else:
            for k in range(10):
                np.add.at(dp, (np.arange(13)*10+k)%13, prev)
        dp %= MOD
    return dp[5]

if __name__ == '__main__':
    ans = main()
    print(ans)
