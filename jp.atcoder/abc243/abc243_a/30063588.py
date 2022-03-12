def main() -> None:
    v, a, b, c = map(int, input().split())
    v %= (a + b + c)
    if v < a:
        print("F")
        return
    v -= a
    if v < b:
        print("M")
        return
    print("T")


if __name__ == "__main__":
    main()
