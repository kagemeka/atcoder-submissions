def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for x in a:
        while x & 1 == 0:
            count += 1
            x >>= 1
    print(count)


if __name__ == "__main__":
    main()
