import typing


def main() -> typing.NoReturn:
    x = int(input())

    a = 100
    for i in range(1 << 20):
        a = a * 101 // 100
        if a >= x:
            print(i + 1)
            return

    raise
main()
