def main() -> None:
    # let 10 ^ n = qm^2 + r
    # [r / m] = [(10 ^ n -  qm^2) / m]
    # = [(10 ^ n) / m) - qm]
    # = [10 ^ n / m] - qm
    # = [10 ^ n / m]

    n, m = map(int, input().split())
    print(pow(10, n, m * m) // m % m)


if __name__ == "__main__":
    main()
