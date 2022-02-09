import sys

mod = 10 ** 9 + 7
n, m, *a = [int(x) for x in sys.stdin.read().split()]

safe = sorted(set(range(1,n+1)) - set(a))
dp = [0] * (n + 2)
dp[0] = 0
dp[1] = 1
for i in safe:
    dp[i+1] = (dp[i] + dp[i-1]) % mod

print(dp[-1])
