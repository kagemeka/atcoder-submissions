import typing
import sys
import numpy as np
import numba as nb


def solve() -> typing.NoReturn:
  ...



def main() -> typing.NoReturn:
  x = int(input())
  if x < 40:
    print(40 - x)
  elif x < 70:
    print(70 - x)
  elif x < 90:
    print(90 - x)
  else:
    print('expert')



main()
