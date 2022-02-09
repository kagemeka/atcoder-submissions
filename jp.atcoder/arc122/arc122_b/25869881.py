import typing
import numpy as np
import sys



def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  a.sort()
  def f(x):
    return (n * x + a.sum() - np.minimum(2 * x, a).sum()) / n

  r = n // 2
  l = (n + 1) // 2 - 1
  m = (a[l] + a[r]) / 2
  x = m / 2
  print(f(x))



def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
