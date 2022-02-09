import typing

def main() -> typing.NoReturn:
    x, y = map(int, input().split())
    print(max(0, (y - x + 10 - 1) // 10))

main()
