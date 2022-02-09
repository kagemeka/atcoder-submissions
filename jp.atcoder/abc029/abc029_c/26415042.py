import typing
import itertools


def main() -> typing.NoReturn:
  n = int(input())
  for p in itertools.product('abc', repeat=n):
    print(''.join(p))


main()
