import typing
import sys
import numpy as np


def solve(l: int) -> typing.NoReturn:
  N = 1 << 8
  choose = np.zeros((N, N), np.int64)
  choose[:, 0] = 1
  for i in range(N - 1):
    choose[i + 1, 1:] = choose[i, 1:] + choose[i, :-1]
  print(choose[l - 1, 11])


def main() -> typing.NoReturn:
  l = int(input())
  solve(l)


main()
