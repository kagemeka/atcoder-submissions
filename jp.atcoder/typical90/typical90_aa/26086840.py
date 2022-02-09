import typing
import sys


def main() -> typing.NoReturn:
  n = int(input())
  s = sys.stdin.read().split()
  buf = set()
  res = []
  for i in range(n):
    if s[i] in buf: continue
    res.append(i + 1)
    buf.add(s[i])
  print(*res, sep='\n')


main()
