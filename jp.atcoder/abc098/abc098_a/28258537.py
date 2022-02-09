import typing

def main() -> typing.NoReturn:
    a, b = map(int, input().split())
    print(max(a + b, a - b, a * b))

main()
