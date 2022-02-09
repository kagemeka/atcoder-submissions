import typing



def main() -> typing.NoReturn:
    a = int(input())
    b = int(input())

    sep = '5' if b & 1 else '0'
    n = ('' if b == 1 else str(b // 2)) + sep + str(a)
    print(n)

main()
