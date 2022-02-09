import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:], nb.i8), cache=True)
def solve(n: int, a: np.ndarray, k: int) -> typing.NoReturn:
  b = np.arange(n)
  for i in a[::-1]:
    b[i], b[i + 1] = b[i + 1], b[i]



  def arr_mul(a, b):
    b = b.copy()
    for i in range(len(a)): b[i] = a[b[i]]
    return b


  def arr_pow(a, k):
    b = np.arange(n)
    while k:
      if k & 1: b = arr_mul(a, b)
      a = arr_mul(a, a)
      k >>= 1
    return b

  b = arr_pow(b, k)
  for x in b:
    print(x + 1)






def main() -> typing.NoReturn:
  n, m, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  ) - 1
  solve(n, a, k)


main()
