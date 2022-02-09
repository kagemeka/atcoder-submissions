import typing
import sys


def main() -> typing.NoReturn:
    n, w = map(int, input().split())
    ab = map(int, sys.stdin.read().split())
    ab = list(zip(*[ab] * 2))
    ab.sort(reverse=True)

    tot = 0
    for a, b in ab:
        if b <= w:
            tot += a * b
            w -= b
            continue
        tot += a * w
        break
    print(tot)

main()
