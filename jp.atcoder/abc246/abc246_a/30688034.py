def main() -> None:
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(x0 ^ x1 ^ x2, y0 ^ y1 ^ y2)


if __name__ == "__main__":
    main()
