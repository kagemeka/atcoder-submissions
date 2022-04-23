def main() -> None:
    s = list(map(int, input()))
    n = len(s)
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(n):
        for j in range(2):
            dp[i + 1][j] = dp[i][j ^ 1] + (s[i] ^ j)
    print(min(dp[-1]))


if __name__ == "__main__":
    main()
