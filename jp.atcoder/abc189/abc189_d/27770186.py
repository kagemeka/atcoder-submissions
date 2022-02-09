import typing
import sys

def main() -> typing.NoReturn:
    n = int(input())
    s = [x == 'AND' for x in sys.stdin.read().split()]

    dp = [[0, 0] for _ in range(n + 1)]
    dp[0] = [1, 1]
    for i in range(n):
        if s[i]:
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][0] = dp[i][1] + 2 * dp[i][0]
        else:
            dp[i + 1][1] = 2 * dp[i][1] + dp[i][0]
            dp[i + 1][0] = dp[i][0]
    print(dp[-1][1])


main()
