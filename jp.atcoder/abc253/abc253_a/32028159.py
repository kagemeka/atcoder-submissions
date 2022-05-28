def main() -> None:
    a, b, c = map(int, input().split())

    d = [a, b, c]
    d.sort()
    print("Yes" if d[1] == b else "No")


if __name__ == "__main__":
    main()
