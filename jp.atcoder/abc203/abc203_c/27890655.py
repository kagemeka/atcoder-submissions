import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0])
    x = k
    for a, b in ab:
        if a <= x:
            x += b
            continue
        print(x)
        return
    print(x)


main()
