def main() -> None:
    a, b, c = map(int, input().split())
    print("YES" if b * 2 == a + c else "NO")


if __name__ == "__main__":
    main()
