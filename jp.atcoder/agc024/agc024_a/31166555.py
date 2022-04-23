def main() -> None:
    a, b, c, k = map(int, input().split())
    print((a - b) * (-1 if k & 1 else 1))


if __name__ == "__main__":
    main()
