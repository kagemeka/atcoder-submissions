def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    diffs = [a[i] - i for i in range(n)]
    grundy_number = 0
    for d in diffs:
        grundy_number ^= d
    print("Alice" if grundy_number != 0 else "Bob")


if __name__ == "__main__":
    main()
