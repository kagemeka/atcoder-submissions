def main() -> None:
    # fermat's little theorem
    n, k, m = map(int, input().split())
    # m^(k^n)

    MOD = 998_244_353

    print(pow(m, pow(k, n, MOD - 1), MOD))


if __name__ == "__main__":
    main()
