def main() -> None:
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))

    # find cycle lengths
    # fibonacci
    MOD = 998_244_353

    pairs = list(zip(p, q))
    pairs.sort()

    checked = [False] * n
    counts = []
    for i in range(n):
        if checked[i]:
            continue
        checked[i] = True
        count = 1
        while not checked[pairs[i][1]]:
            i = pairs[i][1]
            checked[i] = True
            count += 1
        counts.append(count)

    dp = [[0, 1]]
    for _ in range(n):
        dp.append([dp[-1][1], sum(dp[-1]) % MOD])

    p = 1
    for c in counts:
        if c == 1:
            continue
        p *= (sum(dp[c - 1]) + dp[c - 2][1]) % MOD
        p %= MOD
    print(p)


if __name__ == "__main__":
    main()
