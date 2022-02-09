import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  rank = np.argsort(np.argsort(a)[::-1]) + 1
  print(*rank)


main()
