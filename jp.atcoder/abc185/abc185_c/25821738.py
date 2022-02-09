import typing
import sys
import numpy as np



def solve(l: int) -> typing.NoReturn:
  c = 1
  for i in range(11):
    c *= (l - 1 - i) / (11 - i)
  print(round(c))


def main() -> typing.NoReturn:
  l = int(input())
  solve(l)


main()
