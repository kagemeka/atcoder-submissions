import string


def main() -> None:
    s = input()
    n = len(s)
    s = set(s)
    if len(s) != n:
        print("No")
        return

    if not s & set(string.ascii_uppercase):
        print("No")
        return
    if not s & set(string.ascii_lowercase):
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    main()
