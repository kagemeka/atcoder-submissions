import typing
import sys


def main() -> typing.NoReturn:
  s = list(input())
  n = int(input())
  lr = map(lambda x: int(x) - 1, sys.stdin.read().split())
  lr = zip(*[lr] * 2)
  for l, r in lr:
    s[l:r + 1] = s[r:l - 1:-1] if l > 0 else s[r::-1]
  print(''.join(s))


main()
