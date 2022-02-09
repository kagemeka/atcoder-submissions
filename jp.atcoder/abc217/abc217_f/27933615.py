import typing


def pascal(n: int, mod: int) -> typing.List[int]:
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        c[i][0] = 1
    for i in range(1, n):
        for j in range(1, i + 1):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]
            c[i][j] %= mod
    return c


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    h = 2 * n
    are_good = [[False] * h for _ in range(h)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        are_good[a][b] = are_good[b][a] = True

    dp = [[0] * h for _ in range(h + 1)]
    for l in range(h - 1):
        r = l + 1
        dp[l][r] = 1 if are_good[l][r] else 0
    for l in range(1, h + 1):
        for r in range(0, l):
            dp[l][r] = 1


    MOD = 998_244_353
    choose = pascal(1 << 7, MOD)
    for delta in range(3, h, 2):
        for l in range(h - delta):
            r = l + delta
            for i in range(l + 1, r + 1, 2):
                if not are_good[l][i]: continue
                dp[l][r] += dp[l + 1][i - 1] * dp[i + 1][r] * choose[(delta + 1) // 2][(i - l + 1) // 2]
                dp[l][r] %= MOD

    print(dp[0][h - 1])




main()
