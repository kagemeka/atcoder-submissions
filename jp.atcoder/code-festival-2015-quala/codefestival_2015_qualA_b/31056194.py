def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    p = 1
    for x in a[::-1]:
        s += p * x
        p <<= 1
    print(s)


if __name__ == "__main__":
    main()
