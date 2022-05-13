def main() -> None:
    x, y = map(int, input().split())
    if (y - 2 * x) & 1:
        print('No')
        return
    m = (y - 2 * x) // 2
    if not 0 <= m <= x:
        print('No')
        return
    print('Yes')


if __name__ == "__main__":
    main()
