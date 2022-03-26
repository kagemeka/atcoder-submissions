def main() -> None:
    a, b, c, d = map(int, input().split())

    if a < c or a == c and b <= d:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
