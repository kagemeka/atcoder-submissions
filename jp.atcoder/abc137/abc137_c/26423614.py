import typing
import sys
import collections


def main() -> typing.NoReturn:
  n = int(input())
  s = sys.stdin.read().split()

  counter = collections.Counter(
    [''.join(sorted(x)) for x in s],
  )
  cnt = 0
  for v in counter.values():
    cnt += v * (v - 1) // 2
  print(cnt)


main()
