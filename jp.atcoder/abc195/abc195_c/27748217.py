import typing


def main() -> typing.NoReturn:
    n = int(input())
    cnt = 0
    for i in range(3, 16, 3):
        cnt += max(0, n - pow(10, i) + 1)
    print(cnt)


main()
