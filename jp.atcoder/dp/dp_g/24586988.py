import typing
import sys
import numpy as np



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


OJ = 'ONLINE_JUDGE'
if sys.argv[-1] == OJ:
  from numba import njit, i8
  from numba.pycc import CC
  cc = CC('my_module')

  fn = solve
  signature =   (i8, i8[:, :])

  cc.export(
    fn.__name__,
    signature,
  )(fn)

  cc.compile()
  exit(0)


from my_module import solve
main()
