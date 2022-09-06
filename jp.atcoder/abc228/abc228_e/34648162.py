def main() -> None:
    p = 998_244_353
    n, k, m = map(int, input().split())
    res = pow(m, pow(k, n, p - 1), p)
    print(res)


main()
