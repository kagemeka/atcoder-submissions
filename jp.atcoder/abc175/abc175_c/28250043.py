import typing


def main() -> typing.NoReturn:
    x, k, d = map(int, input().split())
    x = abs(x)

    c = x // d
    if k < c:
        print(x - d * k)
        return

    x -= c * d
    k -= c
    if k & 1:
        x = d - x
    print(x)

main()
