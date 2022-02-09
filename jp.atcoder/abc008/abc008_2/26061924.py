import typing
import sys
import collections



def main() -> typing.NoReturn:
  n = int(input())
  s = sys.stdin.read().split()
  cnt = collections.Counter(s)

  res = sorted(cnt.items(), key=lambda x: x[1])
  print(res[-1][0])


main()
