import typing
import math


def main() -> typing.NoReturn:
  x = int(input())

  t = math.ceil((2 * x + 1 / 4) ** .5 - 1 / 2)
  print(t)


main()
