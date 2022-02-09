import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  i = np.argsort(a)[::-1] + 1
  print(*i)


main()
