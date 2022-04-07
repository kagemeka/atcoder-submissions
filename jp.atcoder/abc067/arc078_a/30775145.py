def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    x = a[0]
    y = sum(a) - x
    min_diff = abs(x - y)
    for v in a[1:-1]:
        x += v
        y -= v
        min_diff = min(min_diff, abs(x - y))
    print(min_diff)


if __name__ == "__main__":
    main()
