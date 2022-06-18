def main() -> None:
    # fermat's little theorem
    n, k, m = map(int, input().split())
    # m^(k^n)

    MOD = 998_244_353

    m %= MOD
    print(0 if m == 0 else pow(m, pow(k, n, MOD - 1), MOD))
    # print(pow(m, pow(k, n, MOD - 1), MOD))


if __name__ == "__main__":
    main()
