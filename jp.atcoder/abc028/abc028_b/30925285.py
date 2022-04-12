import collections


def main() -> None:
    s = "ABCDEF"
    count = collections.Counter(input())
    print(*(count[c] for c in s))


if __name__ == "__main__":
    main()
