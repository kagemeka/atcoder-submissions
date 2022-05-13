def solve() -> int:
    MOD = 998_244_353
    n = int(input())
    s = [ord(x) - ord("A") for x in input()]
    if n == 1:
        return s[0] + 1

    m = (n + 1) // 2
    dp = [0] * (m + 1)
    for i in range(m):
        dp[i + 1] = dp[i] * 26 % MOD + s[i]
    dp[-1] %= MOD
    cnt = dp[-1]

    cnt += s[:m] <= s[-m:][::-1]
    cnt %= MOD

    return cnt
    # same/small


def main() -> None:
    t = int(input())
    res = []
    for _ in range(t):
        ret = solve()
        res.append(ret)
    print(*res, sep='\n')


if __name__ == "__main__":
    main()
