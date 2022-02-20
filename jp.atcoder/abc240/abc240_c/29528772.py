

def main() -> None:
    n, x = map(int, input().split())
    k = 1 << 14
    dp = [False] * k
    dp[0] = True
    for _ in range(n):
        ndp = [False] * k
        a, b = map(int, input().split())
        for i in range(x):
            ndp[i + a] |= dp[i]
            ndp[i + b] |= dp[i]
        dp = ndp
    print("Yes" if dp[x] else "No")


if __name__ == "__main__":
    main()
