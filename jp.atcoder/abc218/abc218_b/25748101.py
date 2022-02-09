import typing
import sys


def main() -> typing.NoReturn:
  *p, = map(int, input().split())
  s = [chr(ord('a') + x - 1) for x in p]
  print(''.join(s))


main()
