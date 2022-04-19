import collections


def main() -> None:
    MOD = 998_244_353

    n = int(input())
    a = list(map(int, input().split()))
    s = a.copy()
    for i in range(n - 1):
        s[i + 1] += s[i]

    dp = [0] * n
    # number of subsequences
    prev = collections.defaultdict(int)
    dp[0] = 1  # empty sequence
    for i in range(n - 1):
        j = prev[s[i]]
        prev[s[i]] = i + 1
        dp[i + 1] = dp[i] * 2
        if j != 0:
            dp[i + 1] -= dp[j - 1]
        dp[i + 1] %= MOD
    print(dp[-1])


if __name__ == "__main__":
    main()
