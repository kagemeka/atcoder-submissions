def main() -> None:
    n, a, b = map(int, input().split())
    if a == b:
        print(1)
        return
    if n == 1 or a > b:
        print(0)
        return
    print(b * (n - 1) + a - (b + a * (n - 1)) + 1)


if __name__ == "__main__":
    main()
