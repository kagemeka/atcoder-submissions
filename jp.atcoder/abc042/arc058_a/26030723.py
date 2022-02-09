import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:]), cache=True)
def solve(n: int, d: np.ndarray) -> typing.NoReturn:
  # dislike = np.bincount(d, minlength=10).astype(np.bool8)
  dislike = np.zeros(10, np.bool8)
  for x in d: dislike[x] = True
  at_most = 10 ** 5

  def check_ok(n):
    while n:
      n, r = divmod(n, 10)
      if dislike[r]: return False
    return True

  for x in range(n, at_most):
    if not check_ok(x): continue
    print(x)
    return




def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  d = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, d)


main()
