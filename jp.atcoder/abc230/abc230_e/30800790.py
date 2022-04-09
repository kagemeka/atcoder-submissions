def main() -> None:
    n = int(input())

    # x <= n / i < x + 1
    # n / (x + 1) < i <= n / x

    tot = 0
    x, i = 1, n

    while x * x < n:
        j = n // (x + 1)
        tot += x * (i - j)
        i = j
        x += 1

    for i in range(1, n + 1):
        if i * i > n:
            break
        tot += n // i
    print(tot)


if __name__ == "__main__":
    main()
