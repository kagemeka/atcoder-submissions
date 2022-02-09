import typing


def main() -> typing.NoReturn:
    a, b, n = map(int, input().split())
    ans = a * n // b - a * (n // b)
    print(ans)

main()
