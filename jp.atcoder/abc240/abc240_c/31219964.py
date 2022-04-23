def main() -> None:
    n, x = map(int, input().split())
    K = 1 << 14
    dp = [False] * K
    dp[0] = True
    for _ in range(n):
        a = list(map(int, input().split()))
        ndp = [False] * K
        for d in a:
            for i in range(d, K):
                ndp[i] |= dp[i - d]
        dp = ndp
    print("Yes" if dp[x] else "No")


if __name__ == "__main__":
    main()
