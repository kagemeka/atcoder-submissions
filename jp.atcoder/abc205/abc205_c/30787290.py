def main() -> None:
    a, b, c = map(int, input().split())
    if a == b or abs(a) == abs(b) and c & 1 == 0:
        print("=")
    else:
        print("<" if c & 1 and a < b or c & 1 == 0 and abs(a) < abs(b) else ">")


if __name__ == "__main__":
    main()
