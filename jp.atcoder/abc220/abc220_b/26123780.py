import sys
import typing

import numba as nb
import numpy as np


def solve() -> typing.NoReturn:
  ...


def convert(n, k) -> int:
  d = 1
  s = 0
  while n:
    n, r = divmod(n, 10)
    s += r * d
    d *= k
  return s



def main() -> typing.NoReturn:
  k = int(input())
  a, b = map(int, input().split())
  a = convert(a, k)
  b = convert(b, k)
  print(a * b)


main()
