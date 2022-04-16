import string


def main() -> None:
    print((set(string.digits) - set(input())).pop())


if __name__ == "__main__":
    main()
