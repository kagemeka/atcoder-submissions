def main() -> None:
    n = int(input())
    p = 1
    MOD = 10**9 + 7

    for i in range(1, n + 1):
        p = p * i % MOD
    print(p)


if __name__ == "__main__":
    main()
