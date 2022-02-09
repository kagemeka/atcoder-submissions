import typing
import sys
import numpy as np



import numpy as np
import typing



class CompressArray():
  def retrieve(
    self,
    i: int,
  ) -> int:
    return self.__v[i]


  def __call__(
    self,
    a: np.array,
  ) -> np.array:
    v = np.unique(a)
    self.__v = v
    i = np.searchsorted(v, a)
    return i


def main():
  h, w, n = map(
    int, input().split(),
  )
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2).T

  compress = CompressArray()
  a = compress(a) + 1
  b = compress(b) + 1
  for a, b in zip(a, b):
    print(a, b)


main()
