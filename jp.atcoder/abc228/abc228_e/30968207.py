def main() -> None:
    # fermat's little theorem
    n, k, m = map(int, input().split())
    # m^(k^n)

    MOD = 998_244_353

    m %= MOD
    print(0 if m == 0 else pow(m, pow(k, n, MOD - 1), MOD))
    # k^n % (MOD - 1) might be 0.
    # 0^0 is defined as 1 in Python.
    # but if m == 0, answer shoud be 0
    # (Fermat's Little Theorem cannot be applied when m == 0).


if __name__ == "__main__":
    main()
