import sys
import typing


def main() -> typing.NoReturn:
    n, l = map(int, input().split())
    s = sys.stdin.read().split()
    s.sort()
    print("".join(s))


main()
