# 2019-11-28 15:32:26(JST)
import sys
def main():
    n, *t = map(int, sys.stdin.read().split())
    s = sum(t) // 2
    t.sort()

    dp = [[0] * (s+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(s+1):
            if t[i] <= j:
                dp[i+1][j] = max(dp[i][j], dp[i][j-t[i]] + t[i])
            else:
                dp[i+1][j] = dp[i][j]
    ans = sum(t) - dp[n][s]
    print(ans)

if __name__ == '__main__':
    main()
