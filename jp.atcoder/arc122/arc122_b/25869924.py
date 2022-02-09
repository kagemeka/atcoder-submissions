import typing
import numpy as np
import sys



def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  a.sort()
  def f(x: float) -> float:
    return (n * x + a.sum() - np.minimum(2 * x, a).sum()) / n


  def ternary_search() -> float:
    lo, hi = 0, a.max()
    for _ in range(100):
      x0 = (lo * 2 + hi) / 3
      x1 = (lo + hi * 2) / 3
      if f(x0) <= f(x1):
        hi = x1
      else:
        lo = x0
    return x1

  x = ternary_search()
  print(f(x))




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
