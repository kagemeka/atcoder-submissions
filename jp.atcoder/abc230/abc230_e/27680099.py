import typing

def main() -> typing.NoReturn:
    n = int(input())
    s = 0
    i = 1
    while i * i <= n:
        s += n // i
        i += 1

    x = 1
    while x * x < n:
        s += x * (n // x - n // (x + 1))
        x += 1
    print(s)

main()
