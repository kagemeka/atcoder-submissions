import typing



def main() -> typing.NoReturn:
    n = int(input())
    x = 0
    while int(str(x + 1) * 2) <= n: x += 1
    print(x)

main()
