import typing


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())
    inf = 1 << 60

    grid = [[-inf] * w for _ in range(h)]
    for _ in range(k):
        y, x, v = map(int, input().split())
        y -= 1
        x -= 1
        grid[y][x] = v
    dp = [[0, -inf, -inf, -inf] for _ in range(w + 1)]
    for j in range(w):
        for k in range(4):
            dp[j + 1][k] = dp[j][k]
        if grid[0][j] == -inf: continue
        for k in range(3, 0, -1):
            dp[j + 1][k] = max(dp[j + 1][k], dp[j + 1][k - 1] + grid[0][j])
    for i in range(1, h):
        g = grid[i]
        for j in range(w):
            dp[j + 1][0] = max(max(dp[j + 1]), dp[j][0])
            for k in range(1, 4):
                dp[j + 1][k] = dp[j][k]
            if grid[i][j] == -inf: continue
            for k in range(3, 0, -1):
                dp[j + 1][k] = max(dp[j + 1][k], dp[j + 1][k - 1] + grid[i][j])
    print(max(dp[-1]))

main()
