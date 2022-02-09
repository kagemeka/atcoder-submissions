import typing


def main() -> None:
    n = int(input())
    print('Yes' if -(1 << 31) <= n < (1 << 31) else 'No')


if __name__ == '__main__':
    main()
