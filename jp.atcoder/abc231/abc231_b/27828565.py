import typing
import collections
import sys


def main() -> typing.NoReturn:
    n = int(input())
    cnt = collections.Counter(sys.stdin.read().split())
    a = list(cnt.items())
    a.sort(key=lambda x: x[1])
    print(a[-1][0])

main()
