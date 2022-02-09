import typing
import sys

def main() -> typing.NoReturn:
  n = int(input())
  *a, = map(int, sys.stdin.read().split())
  a = sorted(set(a))
  print(a[-2])


main()
