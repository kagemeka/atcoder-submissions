import typing


def main() -> typing.NoReturn:
    n, avg = map(int, input().split())
    a = list(map(int, input().split()))
    k = n * avg

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for x in a:
        for i in range(n, 0, -1):
            for j in range(x, k + 1):
                dp[i][j] += dp[i - 1][j - x]
    cnt = 0
    for i in range(1, n + 1):
        cnt += dp[i][i * avg]
    print(cnt)

main()
