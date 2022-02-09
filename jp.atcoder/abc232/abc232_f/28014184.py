import typing


def main() -> typing.NoReturn:
    # permutation brute force -> dp (set and last)
    # dp[s][last]
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    inf = 1 << 60
    dp = [[inf] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = abs(b[0] - a[i]) * x
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1: continue
            t = s & ~(1 << i)
            cost = 0
            cnt = 0
            mn = inf
            for j in range(n):
                if ~t >> j & 1: continue
                cost += y * (j > i)
                cnt += 1
                mn = min(mn, dp[t][j])
            cost += abs(b[cnt] - a[i]) * x + mn
            dp[s][i] = min(dp[s][i], cost)

    print(min(dp[-1]))


main()
