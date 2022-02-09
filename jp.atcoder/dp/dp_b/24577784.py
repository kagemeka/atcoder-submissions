import typing
import numpy as np
import numba as nb



@nb.njit(
  (nb.i8, nb.i8, nb.i8[:]),
  cache=True,
)
def solve(
  n: int,
  k: int,
  h: np.array,
) -> typing.NoReturn:
  inf = 1 << 30
  c = np.full(
    n + 1,
    inf,
    dtype=np.int64,
  )
  c[:2] = 0
  for i in range(2, n + 1):
    x = inf
    for j in range(i - k, i):
      if j < 0: continue
      x = min(
        x,
        c[j] + abs(h[i] - h[j])
      )
    c[i] = x
  print(c[n])



def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  *h, = map(
    int, input().split(),
  )
  h = [h[0]] + h
  h = np.array(h)
  solve(n, k, h)



main()
