# 2019-11-23 01:28:44(JST)
import sys
import math

MOD = 998244353

def main():
    n, *a = map(int, sys.stdin.read().split())
    S = sum(a)
    dp = [[0 for _ in range(S+1)] for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for r in range(S+1):
            dp[i+1][r] += dp[i][r] * 2
            if r >= a[i]:
                dp[i+1][r] += dp[i][r-a[i]]

            dp[i+1][r] %= MOD

    # if S % 2 == 0:
    #     ans = (pow(3, n, MOD) - ((sum(dp[n][S//2+1:]) * 3) % MOD)) % MOD
    # else:
    #     ans = (pow(3, n, MOD) - (sum(dp[n][S//2+1:]) * 3 % MOD)) % MOD
    # print(ans)
    ans = (pow(3, n, MOD) - ((sum(dp[n][S//2+1:]) * 3) % MOD)) % MOD
    # Sが奇数だったらこれでいい 偶数だったらさらに、(dp[n][S//2]を３倍して、そこから(R = G = S/2, B = 0) となる場合の数を２倍して引いた通り数) を引けばいい
    if S % 2 == 0:
        ans = (ans - (dp[n][S//2] * 3 - (dp[n][S//2] - dp[n][0]) * 3)) % MOD

    print(ans)


if __name__ == '__main__':
    main()
