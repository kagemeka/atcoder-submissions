import typing

def main() -> typing.NoReturn:
    a, b, c, d, k = map(int, input().split())
    x = a * 60 + b
    y = c * 60 + d
    print(y - x - k)

main()
