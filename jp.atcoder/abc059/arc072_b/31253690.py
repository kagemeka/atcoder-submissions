def main() -> None:
    x, y = map(int, input().split())
    print("Brown" if abs(x - y) <= 1 else "Alice")


if __name__ == "__main__":
    main()
