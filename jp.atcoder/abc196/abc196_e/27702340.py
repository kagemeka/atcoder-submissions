import typing


def main() -> typing.NoReturn:
    n = int(input())
    at = [map(int, input().split()) for _ in range(n)]
    q = int(input())
    x = list(map(int, input().split()))

    inf = 1 << 60
    add = 0
    low = -inf
    high = inf

    for a, t in at:
        if t == 1:
            add += a
            low += a
            high += a
        elif t == 2:
            low = max(low, a)
            high = max(high, low)
        else:
            high = min(high, a)
            low = min(low, high)

    assert low <= high
    for i in x:
        print(min(max(i + add, low), high))

main()
