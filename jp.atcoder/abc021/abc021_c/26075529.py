import typing
import sys
import numpy as np
import numba as nb


# @nb.njit((nb.i8, nb.i8, nb.i8, nb.i8[:, :]), cache=True)
def solve(
  n: int,
  a: int,
  b: int,
  xy: np.ndarray,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  m = len(xy)
  cnt = np.zeros(n, np.int64)
  cnt[a] = 1
  g = np.zeros((n, n), np.int64)
  x, y = xy.T
  g[x, y] = g[y, x] = 1
  while cnt[b] == 0:
    cnt = np.dot(g, cnt) % mod
  print(cnt[b])


def main() -> typing.NoReturn:
  n = int(input())
  a, b = map(lambda x: int(x) - 1, input().split())
  m = int(input())
  xy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, a, b, xy)


main()
