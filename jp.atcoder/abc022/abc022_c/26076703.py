import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def shortest_path_floyd_warshall(g: np.ndarray) -> np.ndarray:
  n = len(g)
  assert g.shape == (n, n)
  g = g.copy()
  for k in range(n):
    for i in range(n):
      for j in range(n):
        g[i, j] = min(g[i, j], g[i, k] + g[k, j])
  return g


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, uvl: np.ndarray) -> typing.NoReturn:
  m = len(uvl)
  inf = 1 << 60
  g = np.full((n, n), inf, np.int64)
  for i in range(m):
    u, v, l = uvl[i]
    g[u, v] = g[v, u] = l


  g[1:, 1:] = shortest_path_floyd_warshall(g[1:, 1:])

  mn = inf
  for i in range(1, n - 1):
    for j in range(i + 1, n):
      d = g[0, i] + g[i, j] + g[j, 0]
      mn = min(mn, d)

  if mn == inf:
    print(-1)
  else:
    print(mn)



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  uvl = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 3)
  uvl[:, :2] -= 1
  solve(n, uvl)

main()
