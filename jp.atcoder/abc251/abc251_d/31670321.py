def main() -> None:
    w = int(input())
    K = 1_000_000
    N = 300

    # base 100
    # 1 - 99
    # 100 - 9900
    # 10000 - 990000

    a = []
    for i in range(1, 100):
        a.append(i)
        a.append(i * 100)
        a.append(i * 10000)

    print(len(a))
    print(*a)


if __name__ == "__main__":
    main()
