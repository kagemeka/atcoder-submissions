def main() -> None:
    p = 998_244_353
    n, k, m = map(int, input().split())
    if m % p == 0:
        print(0)
        return
    res = pow(m, pow(k, n, p - 1), p)
    print(res)


main()
