import typing


def main() -> typing.NoReturn:
    x, k, d = map(int, input().split())
    x = abs(x)
    c = x // d
    if c > k:
        print(x - d * k)
        return
    x -= d * c
    k -= c
    k &= 1
    x -= d * k
    print(abs(x))

main()
