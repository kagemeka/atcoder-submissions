import typing
import sys
import numpy as np


def main() -> typing.NoReturn:
  s, e = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(-1, 2).T
  print(np.sum(s // 10 * e))

main()
