import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:, :], ), cache=True)
def floyd_warshall(g: np.ndarray) -> typing.NoReturn:
  n = len(g)
  assert g.shape == (n, n)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit
def csgraph_to_dense(n: int, g: np.ndarray, fill: int) -> np.ndarray:
  m = len(g)
  assert g.shape == (m, 3)
  t = np.full((n, n), fill, np.int64)
  for i in range(m): t[g[i, 0], g[i, 1]] = g[i, 2]
  return t


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, abt: np.ndarray) -> typing.NoReturn:
  inf = 1 << 60
  g = csgraph_to_dense(n, csgraph_to_directed(abt), inf)
  for i in range(n): g[i, i] = 0
  floyd_warshall(g)
  mn = inf
  for i in range(n): mn = min(mn, g[i].max())
  print(mn)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  abt = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(m, 3)
  abt[:, :2] -= 1
  solve(n, abt)

main()
