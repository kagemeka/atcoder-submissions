import typing

def main() -> typing.NoReturn:
    a, b, c = map(int, input().split())
    print(c // min(a, b))

main()
