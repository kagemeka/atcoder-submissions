import typing
import collections
import sys


def main() -> typing.NoReturn:
    n = int(input())
    cnt = collections.Counter(sys.stdin.read().split())
    for judge in ['AC', 'WA', 'TLE', 'RE']:
        print(f'{judge} x {cnt[judge]}')


main()
