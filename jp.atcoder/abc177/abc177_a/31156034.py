def main() -> None:
    d, t, s = map(int, input().split())
    print("Yes" if d <= t * s else "No")


if __name__ == "__main__":
    main()
