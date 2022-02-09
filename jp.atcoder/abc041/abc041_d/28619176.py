import typing


def main() -> None:
    n, m = map(int, input().split())

    in_deg = [0] * n
    before = [0] * n
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        in_deg[y] += 1
        before[y] |= 1 << x

    dp = [0] * (1 << n)
    dp[0] = 1
    for s in range(1 << n):
        for i in range(n):
            if ~s >> i & 1:
                continue
            t = s & ~(1 << i)
            if before[i] & ~t == 0:
                dp[s] += dp[t]
    print(dp[-1])

main()
