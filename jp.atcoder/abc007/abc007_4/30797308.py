def count(n: int) -> int:
    n0 = n
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10

    digits.reverse()
    dp = [1, 0]
    for d in digits:
        dp[1] = dp[1] * 8 + dp[0] * (d - (d > 4))
        if d == 4 or d == 9:
            dp[0] = 0
    return n0 - sum(dp)


def main() -> None:
    a, b = map(int, input().split())
    print(count(b) - count(a - 1))


if __name__ == "__main__":
    main()
