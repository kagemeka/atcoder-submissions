import typing

def main() -> typing.NoReturn:
    a = int(input())
    b = int(input())
    c = (a + b) % 12
    if c == 0: c += 12
    print(c)

main()
