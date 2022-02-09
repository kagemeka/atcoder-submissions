import typing
import sys
import numpy as np
import numba as nb
import itertools



def solve(
  n: int,
  m: int,
  p: int,
  q: int,
  xyz: np.ndarray,
) -> typing.NoReturn:
  g = np.zeros((n, m), np.int64)
  x, y, z = xyz.T
  g[x, y] = z

  s = np.array(
    [*itertools.combinations(range(n), p)],
    dtype=np.int64,
  )
  mx = np.sort(
    g[s].sum(axis=1),
    axis=1,
  )[:, -q:].sum(axis=1).max()
  print(mx)


def main() -> typing.NoReturn:
  n, m, p, q, r = map(int, input().split())
  xyz = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(r, 3)
  xyz[:, :2] -= 1
  solve(n, m, p, q, xyz)


main()
