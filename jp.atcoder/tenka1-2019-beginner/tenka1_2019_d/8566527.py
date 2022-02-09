# 2019-11-23 01:28:44(JST)
import sys
import numpy as np

MOD = 998244353

def main():
    n, *A = map(int, sys.stdin.read().split())
    S = sum(A)

    dp = np.zeros(S//2+1, dtype=np.int64)
    dp[0] = 1
    for a in A:
        dp[a:] = (dp[a:] + dp.copy()[:-a] * 2) % MOD

    ans = (pow(3, n, MOD) - dp.sum() * 3 % MOD) % MOD

    if S % 2 == 0:
        dp = np.zeros(S//2+1, dtype=np.int64)
        dp[0] = 1
        for a in A:
            dp[a:] = (dp[a:] + dp.copy()[:-a]) % MOD
        ans = (ans + dp[S//2] * 3) % MOD

    print(ans)


if __name__ == '__main__':
    main()
