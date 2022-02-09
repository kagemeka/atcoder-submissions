import typing
import sys


def main() -> typing.NoReturn:
  n = int(input())
  ng = set(map(int, sys.stdin.read().split()))

  for _ in range(100):
    if n in ng: break
    for i in range(3, 0, -1):
      if n - i in ng: continue
      n -= i
      break
    else: break
    if n <= 0:
      print('YES')
      return

  print('NO')


main()
