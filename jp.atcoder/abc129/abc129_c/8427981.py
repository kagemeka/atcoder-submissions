import sys

mod = 10 ** 9 + 7
n, m, *a = [int(x) for x in sys.stdin.read().split()]

dp = [0] * (n + 2)
dp[0] = 0
dp[1] = 1
for i in range(2, n+2):
    if i - 1 in a:
        if dp[i-1] == 0:
            print(0)
            sys.exit()
        else:
            dp[i] = 0
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[-1])
