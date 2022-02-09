import typing


def main() -> typing.NoReturn:
    n = int(input())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n - 1)]

    s = sum((i + 1) * (n - i) for i in range(n))
    for u, v in uv:
        if u > v: u, v = v, u
        s -= (u + 1) * (n - v)
    print(s)

main()
