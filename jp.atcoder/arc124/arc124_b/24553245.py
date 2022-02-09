import typing
import numpy as np
import sys


def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n)
  x = np.unique(a[0] ^ b)
  x.sort()
  ok = np.sort(
    x[:, None] ^ a,
    axis=1,
  ) == np.sort(b)
  x = x[ok.all(axis=1)]
  n = x.size
  print(n)
  if n: print(*x, sep='\n')


main()
