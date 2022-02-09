import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ab.sort()
    cost = 0
    for a, b in ab:
        if b >= m:
            cost += a * m
            break
        cost += a * b
        m -= b
    print(cost)

main()
