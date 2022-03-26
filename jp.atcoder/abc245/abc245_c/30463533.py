def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[False, False] for _ in range(n)]
    dp[0] = [True, True]
    for i in range(n - 1):
        dp[i + 1][0] |= dp[i][0] and abs(a[i + 1] - a[i]) <= k
        dp[i + 1][0] |= dp[i][1] and abs(a[i + 1] - b[i]) <= k
        dp[i + 1][1] |= dp[i][0] and abs(b[i + 1] - a[i]) <= k
        dp[i + 1][1] |= dp[i][1] and abs(b[i + 1] - b[i]) <= k

    print("Yes" if dp[-1][0] or dp[-1][1] else "No")


if __name__ == "__main__":
    main()
