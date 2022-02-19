import sys
import typing

import numba as nb
import numpy as np


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
