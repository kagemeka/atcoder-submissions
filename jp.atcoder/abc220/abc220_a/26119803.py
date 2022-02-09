import typing
import sys
import numpy as np
import numba as nb


def solve() -> typing.NoReturn:
  ...

def main() -> typing.NoReturn:
  a, b, c = map(int, input().split())
  for i in range(a, b + 1):
    if i % c == 0:
      print(i)
      return
  print(-1)




main()
