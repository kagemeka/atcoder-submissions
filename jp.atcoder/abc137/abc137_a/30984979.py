def main() -> None:
    a, b = map(int, input().split())
    print(max(a + b, a - b, a * b))


if __name__ == "__main__":
    main()
