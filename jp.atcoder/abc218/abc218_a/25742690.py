import sys
import typing


def main() -> typing.NoReturn:
  n = int(input())
  s = input()
  if s[n - 1] == 'o':
    print('Yes')
  else:
    print('No')


main()
