import typing

def main() -> typing.NoReturn:
    a, b, c, k = map(int, input().split())
    a = [1] * a + [0] * b + [-1] * c
    print(sum(a[:k]))

main()
