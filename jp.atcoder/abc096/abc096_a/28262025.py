import typing

def main() -> typing.NoReturn:
    a, b = map(int, input().split())
    print(a if b >= a else a - 1)

main()
