import typing


def main() -> typing.NoReturn:
    x = input()
    n = int(input())
    a = [input() for _ in range(n)]
    idx = dict(zip(x, range(26)))
    b = [tuple(map(lambda c: idx[c], s)) for s in a]
    res = sorted(zip(a, b), key=lambda x: x[1])
    for s, _ in res:
        print(s)

main()
