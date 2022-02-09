import typing
import sys
import numpy as np
import numba as nb

@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  g: np.array,
) -> typing.NoReturn:
  indeg = np.zeros(
    n,
    dtype=np.int64,
  )
  for v in g[:, 1]:
    indeg[v] += 1
  g = g[g[:, 0].argsort()]
  i = np.searchsorted(
    g[:, 0],
    np.arange(n + 1)
  )
  q = [
    v for v in range(n)
    if not indeg[v]
  ]
  dist = np.zeros(
    n,
    dtype=np.int64,
  )
  for u in q:
    for j in range(
      i[u], i[u + 1],
    ):
      v = g[j, 1]
      indeg[v] -= 1
      dist[v] = max(
        dist[v],
        dist[u] + 1,
      )
      if indeg[v]: continue
      q.append(v)

  print(dist.max())



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  g = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2) - 1
  solve(n, g)


main()
