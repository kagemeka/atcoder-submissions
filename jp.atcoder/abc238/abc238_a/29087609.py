import typing


def main() -> None:
    n = int(input())
    if n == 1:
        print('Yes')
        return
    print("Yes" if n > 4 else "No")


if __name__ == "__main__":
    main()
