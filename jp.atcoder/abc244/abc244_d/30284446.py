def main() -> None:
    s = list(input())
    t = list(input())
    diff = sum(s[i] != t[i] for i in range(len(s)))
    print('Yes' if diff != 2 else 'No')


if __name__ == "__main__":
    main()
