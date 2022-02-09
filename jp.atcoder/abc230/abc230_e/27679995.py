import typing

def main() -> typing.NoReturn:
    n = int(input())
    i = 1
    s = 0
    while i <= n:
        x = n // i
        j = n // x + 1
        s += x * (j - i)
        i = j
    print(s)

main()
