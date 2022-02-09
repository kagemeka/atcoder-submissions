import typing


def main() -> typing.NoReturn:
    n = int(input())
    xyz = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 60
    dist = [[inf] * n for _ in range(n)]
    for i in range(n):
        a, b, c = xyz[i]
        for j in range(n):
            x, y, z = xyz[j]
            d = abs(x - a) + abs(y - b)
            dist[i][j] = d + max(0, z - c)
            dist[j][i] = d + max(0, c - z)


    dp = [[inf] * n for _ in range(1 << n)]
    dp[1 << 0][0] = 0
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1: continue
            t = s & ~(1 << i)
            for j in range(n):
                if ~t >> j & 1: continue
                dp[s][i] = min(dp[s][i], dp[t][j] + dist[j][i])

    mn = min(dp[-1][i] + dist[i][0] for i in range(1, n))
    print(mn)

main()
