def main() -> None:
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    else:
        if x > b:
            print(0)
        else:
            print(c / (b - a))


if __name__ == '__main__':
    main()
