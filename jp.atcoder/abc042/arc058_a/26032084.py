import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8[:]), cache=True)
def solve(n: int, d: np.ndarray) -> typing.NoReturn:
  like = np.ones(10, np.bool8)
  like[d] = False
  like = np.flatnonzero(like)

  def enumerate_numbers():
    cand = np.empty(1 << 20, np.int64)
    i = 0
    que = [(0, 0)]
    for x, p in que:
      if p == 5: continue
      if p >= 1 and x == 0: continue
      for y in like:
        nx = x * 10 + y
        cand[i] = nx
        i += 1
        que.append((nx, p + 1))
    return cand[:i]

  cand = enumerate_numbers()
  ans = cand[np.searchsorted(cand, n)]
  print(ans)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  d = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, d)


main()
