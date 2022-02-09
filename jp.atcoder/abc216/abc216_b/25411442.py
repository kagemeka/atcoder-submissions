import typing
import sys
import collections


def main() -> typing.NoReturn:
  n = int(input())
  a = sys.stdin.read().split()
  a = zip(*[iter(a)] * 2)
  c = collections.Counter(a)
  if any(v >= 2 for v in c.values()):
    print('Yes')
  else:
    print('No')


main()
