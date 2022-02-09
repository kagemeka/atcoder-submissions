import typing
import sys


def main() -> typing.NoReturn:
  cand = {
    'ABC',
    'ARC',
    'AGC',
    'AHC',
  }
  s = set(sys.stdin.read().split())
  cand -= s
  print(cand.pop())


main()
