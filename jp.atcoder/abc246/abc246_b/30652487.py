def main() -> None:
    a, b = map(int, input().split())
    d = (a ** 2 + b ** 2) ** 0.5
    x, y = a / d, b / d
    print(x, y)


if __name__ == "__main__":
    main()
